import os
from dotenv import load_dotenv
from google import genai

from utils.logger import logger

load_dotenv()

api_key = os.getenv(
    "GEMINI_API_KEY"
)

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found."
    )

client = genai.Client(
    api_key=api_key
)

MODELS = [
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.5-pro"
    
]


def generate_response(prompt):
    last_error = None

    for model in MODELS:
        try:
            response = (
                client.models.generate_content(
                    model=model,
                    contents=prompt
                )
            )

            logger.info(
                f"Response generated using {model}"
            )

            return response.text

        except Exception as e:

            logger.error(
                f"{model} failed: {e}"
            )

            print(
                f"{model} failed:",
                e
            )

            last_error = str(e)

    return (
        f"All Gemini models failed: "
        f"{last_error}"
    )