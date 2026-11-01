from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

caminho_pdf = "data/políticas_da_loja.pdf"

try:
    # 1. Carrega o documento bruto
    loader = PyPDFLoader(caminho_pdf)
    paginas = loader.load()
    print(f"✅ PDF carregado: {len(paginas)} páginas.")

    # 2. Configura o "Cortador" (Splitter)
    # Ele tenta manter parágrafos juntos, fatiando em blocos de até 1000 caracteres
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200, 
        separators=["\n\n", "\n", " ", ""] 
    )

    # 3. Fatiar o documento
    blocos = text_splitter.split_documents(paginas)

    print(f"✂️ O documento foi dividido em {len(blocos)} blocos estruturados.")
    
    print("\n--- Amostra do Primeiro Bloco (Limpo) ---")
    # Limpamos as quebras de linha visuais apenas para ficar bonito no terminal
    texto_limpo = blocos[0].page_content.replace('\n', ' ')
    print(texto_limpo)

except Exception as e:
    print(f"\n❌ Erro: {e}")