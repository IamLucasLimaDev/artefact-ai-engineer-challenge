import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Carrega as credenciais seguras (precisamos da chave para a API de embeddings)
load_dotenv()

caminho_pdf = "data/políticas_da_loja.pdf"

try:
    # 2. Carrega e fatia o PDF (O que já fizemos com sucesso)
    loader = PyPDFLoader(caminho_pdf)
    paginas = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    blocos = text_splitter.split_documents(paginas)
    print(f"✅ PDF dividido em {len(blocos)} blocos.")

    # 3. Converte o texto para matemática (Embeddings)
    print("🧠 A gerar as coordenadas matemáticas (Embeddings)...")
    # text-embedding-004 é o modelo mais recente e otimizado da Google para este fim
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
    # 4. Cria o Banco de Dados Vetorial e insere os blocos lá dentro
    vector_store = FAISS.from_documents(blocos, embeddings)

    # 5. Guarda o banco de dados no seu disco rígido
    vector_store.save_local("faiss_index")
    print("💾 Banco de dados FAISS guardado com sucesso na pasta 'faiss_index'!")

except Exception as e:
    print(f"\n❌ Erro: {e}")