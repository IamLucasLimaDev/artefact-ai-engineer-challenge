import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
chave = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=chave)

print("\n--- Modelos de TEXTO (generateContent) Disponíveis para esta Chave ---")
try:
    encontrou = False
    for m in genai.list_models():
        # Agora procuramos por 'generateContent'
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
            encontrou = True
            
    if not encontrou:
        print("Nenhum modelo de texto encontrado para esta chave.")
except Exception as e:
    print(f"Erro ao listar modelos: {e}")