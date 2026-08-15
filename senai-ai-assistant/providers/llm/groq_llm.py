import groq
from config.settings import (LLM_MODEL, LLM_TEMP, GROQ_API_KEY)

# Instanciando o client do groq

client = groq.Groq(api_key=GROQ_API_KEY)

def chat(prompt: str, contexto: list[dict]) -> str:
    cliente = client.chat.completions.create(
        messages=contexto,
        model=LLM_MODEL,
        temperature=float(LLM_TEMP)
    )
    return cliente.choices[0].message.content