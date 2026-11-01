# 🎸 Protótipo: Agente de Atendimento - Empório da Música

Este projeto é um protótipo de Inteligência Artificial desenvolvido para auxiliar o atendimento ao cliente da loja fictícia Empório da Música. O sistema utiliza a arquitetura RAG (Retrieval-Augmented Generation) para responder a dúvidas sobre políticas da loja, baseando-se estritamente num manual em formato PDF.

## 🏗️ Arquitetura do Sistema

A solução foi construída utilizando as seguintes tecnologias:
*   **Backend / API:** Flask (Python) para orquestrar as requisições entre o frontend e os modelos de IA.
*   **Frontend:** Interface de utilizador integrada numa *Landing Page* estática (HTML/CSS/JS), simulando o ambiente real de um e-commerce.
*   **Processamento de Linguagem Natural (LLM):** `gemini-3.8-flash` via LangChain para geração de respostas contextuais.
*   **Base de Dados Vetorial:** FAISS para armazenamento e busca semântica, utilizando embeddings gerados pelo modelo `gemini-embedding-2`.
*   **Extração de Dados:** `pypdf` para leitura e fragmentação do manual da loja.

## 🚀 Como Executar o Projeto Localmente

1.  **Clone o repositório e aceda à pasta:**
    ```bash
    git clone [https://github.com/IamLucasLimaDev](https://github.com/IamLucasLimaDev)
    cd artefact-test
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    *   Crie um ficheiro chamado `.env` na raiz do projeto.
    *   Adicione a sua chave de API da Google:
        ```text
        GOOGLE_API_KEY=sua_chave_aqui
        ```

5.  **Inicie o servidor:**
    ```bash
    python app.py
    ```

6.  **Aceda à aplicação:**
    *   Abra o seu navegador e vá a `http://127.0.0.1:5000`.
    *   Clique no botão flutuante de chat no canto inferior direito e faça uma pergunta!
  
 ## 🤖 Uso de Inteligência Artificial e Workflow

Este projeto foi desenvolvido utilizando uma abordagem moderna de engenharia, onde assistentes de código e IA generativa foram empregados como ferramentas de alavancagem de produtividade. O objetivo foi minimizar o tempo gasto em código *boilerplate* (repetitivo) e focar o esforço humano na orquestração do pipeline de Inteligência Artificial (RAG) e na integração do backend.

**Ferramentas Utilizadas:**
*   **Google Gemini (Chat):** Utilizado como *Thought Partner* (parceiro de raciocínio) e *Pair Programming*. 
*   **Assistente de Geração de UI (ex: v0/Claude):** Utilizado exclusivamente para a prototipagem visual do frontend.

**Como a IA foi explorada no Workflow:**
1.  **Delegação de Frontend:** A construção da Landing Page (HTML/CSS com Tailwind) e a lógica de UI do chat flutuante foram geradas por IA. Isso permitiu entregar uma interface comercial e responsiva sem desviar o foco do objetivo principal do teste (o backend inteligente).
2.  **Troubleshooting e Debugging Avançado:** O Gemini foi utilizado para analisar *tracebacks* complexos durante o desenvolvimento, como a resolução de problemas de concorrência (*Threading*) entre o Flask e a API do LangChain, além do mapeamento de limites de requisição (*Rate Limits* 429) e identificação dos modelos suportados pela chave da API.
3.  **Refinamento de Arquitetura:** Discussões de design de software para a escolha do banco de dados (optando pelo armazenamento vetorial em memória com FAISS em detrimento de bancos relacionais, mantendo a simplicidade exigida por um MVP).
4.  **Design do PromptTemplate:** Auxílio na formatação das travas de segurança (guardrails) para garantir que o agente respondesse *apenas* com base no contexto do PDF fornecido, mitigando alucinações.