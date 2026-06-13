def tutor_prompt(
    query,
    context
):
    return f"""
You are Tutor Agent.

Use ONLY the provided context.

Context:
{context}

Question:
{query}

Instructions:

1. Give a direct answer.
2. Explain clearly.
3. Give examples.
4. Provide key takeaways.
5. If information is insufficient,
   explicitly say so.

Response:
"""