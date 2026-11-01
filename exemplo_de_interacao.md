# 💬 Exemplos de Interação com o Agente

Abaixo estão documentados 4 cenários reais de interação com o agente da Empório da Música, demonstrando a sua capacidade de aplicar regras de negócio via RAG e as suas travas de segurança (guardrails) para não alucinar informações ausentes no contexto.

---

### Cenário 1: Aplicação de Políticas de Devolução (Não-trivial)
**Objetivo:** Demonstrar a extração e interpretação de regras específicas do documento PDF.

**Usuário:** Me arrependi da minha compra, posso devolver meu pedido?
**Agente:** Olá! Sim, de acordo com as nossas políticas, você pode solicitar a devolução por arrependimento em até **7 (sete) dias corridos** após o recebimento do produto, sem necessidade de justificativa. O instrumento deve estar na embalagem original, sem sinais de uso e com todos os manuais. O frete de devolução é por conta da loja e o reembolso ocorre em até 10 dias úteis. Para iniciar o processo, por favor, envie um e-mail para contato@emporiodamusica.com.br.

---

### Cenário 2: Tratamento de Exceções da Política (Não-trivial)
**Objetivo:** Mostrar que o agente entende as nuances e exceções das regras da loja.

**Usuário:** Mandei fazer uma guitarra sob medida com vocês, mas não gostei da cor. Posso devolver pelo direito de arrependimento?
**Agente:** Sinto muito, mas não é possível realizar a devolução. Instrumentos com personalizações ou ajustes sob encomenda (como setup ou regulagem especial) não são elegíveis para devolução ou troca, sendo considerados de "venda final". Caso tenha alguma dúvida adicional, peço que envie um e-mail para contato@emporiodamusica.com.br.

---

### Cenário 3: Prevenção de Alucinação em Catálogo (Segurança do Prompt)
**Objetivo:** Validar a instrução restritiva do *PromptTemplate*. Como o agente não tem acesso a um banco de dados SQL com estoque em tempo real (apenas ao PDF de políticas), ele deve recusar-se a inventar preços.

**Usuário:** Quais opções de violões disponíveis custando até R$1000?
**Agente:** Desculpe, mas não tenho acesso ao catálogo de produtos, preços ou disponibilidade de estoque no momento, pois sou um assistente focado nas políticas e suporte da loja. Para consultar as opções de violões até R$1000,00, por favor, envie um e-mail para contato@emporiodamusica.com.br e a nossa equipe de vendas terá todo o prazer em ajudar!

---

### Cenário 4: Informações Gerais
**Objetivo:** Consulta de informações institucionais básicas.

**Usuário:** Qual o endereço da loja física de vocês?
**Agente:** A Empório da Música está localizada na Rua 14 de Maio, 3200 - Centro, Campo Grande - MS. Será um prazer receber a sua visita!