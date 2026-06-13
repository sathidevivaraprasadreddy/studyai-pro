def assessment_prompt(content):

    return f"""
You are Assessment Agent.

Generate a complete assessment.

Content:
{content}

Create:

10 MCQs

5 Short Answer Questions

5 Long Answer Questions

Include Answer Key.
"""