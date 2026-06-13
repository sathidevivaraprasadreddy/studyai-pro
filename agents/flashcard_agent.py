def generate_flashcards_prompt(content):

    return f"""
You are Flashcard Agent.

Create flashcards.

Content:
{content}

Format:

Question:
Answer:

Generate at least 20 flashcards.
"""