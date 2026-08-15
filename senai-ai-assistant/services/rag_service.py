# services/rag_service.py
from services.embedding_service import (
    generate_embedding
)

from services.vector_store import search
from services.llm_service import chat

def retrieve_context(
        question,
        index,
        chunks):

    question_embedding = (
        generate_embedding(question)
    )

    positions = search(
        index,
        question_embedding
    )

    context_parts = []

    for pos in positions:

        context_parts.append(
            chunks[pos]
        )

    return "\n".join(context_parts)
    
def build_prompt(
        context,
        question):

    return f"""
Você deve responder
utilizando apenas as
informações do contexto.

Contexto:

{context}

Pergunta:

{question}

Se a resposta não estiver
no contexto, informe que
não encontrou a informação.
"""

def ask_question(
        question,
        index,
        chunks):

    context = retrieve_context(
        question,
        index,
        chunks
    )

    prompt = build_prompt(
        context,
        question
    )

    return chat(prompt)