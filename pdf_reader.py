from langchain_community.document_loaders import PyPDFLoader

caminho_pdf = "data/políticas_da_loja.pdf"
print(f"Fazendo a leitura do documento{caminho_pdf}... ")

try:
    # 2. Carrega o documento e divide-o automaticamente por páginas
    loader = PyPDFLoader(caminho_pdf)
    paginas = loader.load()

    # 3. Imprime um resumo do que o Python conseguiu ler
    print("\n✅ PDF carregado com sucesso!")
    print(f"Número total de páginas encontradas: {len(paginas)}")
    
    print("\n--- Conteúdo da Primeira Página (Amostra) ---")
    # Vamos imprimir apenas os primeiros 300 caracteres para não poluir o terminal
    print(paginas[0].page_content[:300] + "...\n")

except Exception as e:
    print(f"\n❌ Erro ao ler o PDF: {e}")