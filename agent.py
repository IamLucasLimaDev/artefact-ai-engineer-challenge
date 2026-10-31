import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()#carrega a chave api

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
parser = StrOutputParser()

cadeia = llm | parser


print("iniciando conexao com o Gemini...")
resposta = cadeia.invoke("aja como assistente virtual da loja 'imperio da musica'. Diga ola de forma educada! ")

print ("\n--- resposta do agente ---")
print (resposta )