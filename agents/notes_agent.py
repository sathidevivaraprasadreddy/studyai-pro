def generate_notes_prompt(content):

    return f"""
You are Notes Agent.

Create revision notes.

Content:
{content}

Include:

1. Summary
2. Important Concepts
3. Key Formulas
4. Exam Tips
5. Important Questions
"""