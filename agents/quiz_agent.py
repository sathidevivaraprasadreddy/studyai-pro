def generate_quiz_prompt(content):

    return f"""
You are Quiz Agent.

Generate 15 multiple-choice questions based ONLY on the provided content.

Content:
{content}

Instructions:
- Create meaningful questions from the content.
- Each question must have exactly 4 options.
- Provide the correct answer.
- Assign a difficulty level (Easy, Medium, or Hard).
- Do not repeat questions.
- Do not leave any field empty.

Output Format:

Q1. [Question Text]

A) Option A
B) Option B
C) Option C
D) Option D

Answer: A

Difficulty: Easy

Q2. [Question Text]

A) Option A
B) Option B
C) Option C
D) Option D

Answer: B

Difficulty: Medium

Continue until Q15.
"""