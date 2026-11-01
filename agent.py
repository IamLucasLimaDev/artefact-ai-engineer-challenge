import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough

# 1. Carrega as credenciais
load_dotenv()

# 2. Instancia os dois motores que configurámos
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")

# 3. Carrega o nosso "Cérebro" (Banco de Dados FAISS)
# allow_dangerous_deserialization=True é necessário por segurança no LangChain para carregar arquivos locais
vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Transformamos o banco de dados num "Retriever" (Buscador). Ele vai pegar os 3 blocos mais relevantes.
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 4. Criamos a Regra de Ouro (O Prompt)
template = """Você é o assistente virtual da loja Empório da Música.
Responda à pergunta do cliente de forma educada, usando APENAS as informações fornecidas no Contexto abaixo.
Se a resposta não estiver no Contexto, diga que não sabe ou peça para o cliente enviar um e-mail para contato@emporiodamusica.com.br.

Contexto da Loja:
{context}

Pergunta do Cliente:
{question}

Sua Resposta:"""
prompt = PromptTemplate.from_template(template)

# Função auxiliar para juntar os blocos de texto encontrados
def formatar_documentos(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 5. A Linha de Montagem Final (Pipeline RAG)
cadeia_rag = (
    {"context": retriever | formatar_documentos, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 6. O Loop de Chat para testarmos no terminal
print("🤖 Assistente da Empório da Música pronto! (Digite 'sair' para encerrar)\n")

while True:
    pergunta_cliente = input("Você: ")
    
    if pergunta_cliente.lower() == 'sair':
        print("Encerrando o chat...")
        break
        
    print("Agente: A pesquisar nas políticas da loja...\n")
    # O invoke agora recebe a pergunta, pesquisa no PDF e gera a resposta!
    resposta = cadeia_rag.invoke(pergunta_cliente)
    
    print(f"Agente: {resposta}\n")