import ollama
import json


def extract_data_with_llm(text):

    prompt = f"""
    Extract the following fields from this document:

    - invoice_number
    - amount
    - date

    Return ONLY valid JSON.

    Document:
    {text}
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response["message"]["content"]

    return result