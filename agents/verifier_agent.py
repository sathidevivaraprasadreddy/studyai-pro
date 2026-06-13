def verify_prompt(answer):

    return f"""
You are Verification Agent.

Review the answer.

Tasks:

1. Correct mistakes.
2. Improve clarity.
3. Remove hallucinations.
4. Keep factual consistency.

Answer:
{answer}

Improved Answer:
"""