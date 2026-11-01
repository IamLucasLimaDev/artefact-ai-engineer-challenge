import os
from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough

app = Flask(__name__)
load_dotenv()

# Isolámos a criação do agente numa função para ser chamada a cada mensagem,
# garantindo que a ligação à Google é feita na mesma "Thread" da pergunta.
def obter_agente_rag():
    # Usamos o gemini-pro (o modelo de texto mais universal e seguro para evitar o 404)
    llm = ChatGoogleGenerativeAI(model="models/gemini-3.8-flash")    # Mantemos o modelo de embeddings exato que usou para criar a base de dados
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
    
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    template = """Você é o assistente virtual da loja Empório da Música.
    Responda à pergunta do cliente de forma educada, usando APENAS as informações fornecidas no Contexto abaixo.
    Se a resposta não estiver no Contexto, diga que não sabe ou peça para o cliente enviar um e-mail para contato@emporiodamusica.com.br.

    Contexto da Loja:
    {context}

    Pergunta do Cliente:
    {question}

    Sua Resposta:"""
    prompt = PromptTemplate.from_template(template)
    
    def formatar_documentos(docs):
        return "\n\n".join(doc.page_content for doc in docs)
        
    return (
        {"context": retriever | formatar_documentos, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

@app.route('/')
def index():
    return send_file('emporio-da-musica.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    dados = request.json
    pergunta_cliente = dados.get('message', '')
    
    if not pergunta_cliente:
        return jsonify({'reply': 'Mensagem vazia.'}), 400

    try:
        # A cada pergunta, geramos uma ligação limpa e fresca
        cadeia_rag = obter_agente_rag()
        resposta = cadeia_rag.invoke(pergunta_cliente)
        return jsonify({'reply': resposta})
    except Exception as e:
        print(f"\nErro no processamento do RAG: {e}\n")
        return jsonify({'reply': 'Desculpe, estou com problemas de ligação aos servidores no momento. Pode tentar novamente em alguns segundos?'}), 500

if __name__ == '__main__':
    print("🚀 Servidor rodando! Acesse http://127.0.0.1:5000 no seu navegador.")
    # A Mágica: threaded=False obriga o Flask a funcionar de forma linear, tal como o agent.py
    app.run(debug=True, threaded=False)