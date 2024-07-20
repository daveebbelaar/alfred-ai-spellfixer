import requests
import sys
import os

# Your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = """
You are an AI assistant whose primary responsibility is to take a text selection and spell correct it. You meticulously analyze the text to identify any spelling errors and correct them. Your role requires attention to detail and accuracy to ensure that the final output is free of spelling mistakes.

Follow these steps:
1. Carefully read through the provided text selection.
2. Identify any words that are misspelled.
3. Correct the spelling of the identified words.
4. Review the corrected text to ensure no spelling errors remain.

Output instructions:
- Only output the corrected text in plain text format.
- Provide the corrected text selection in a clean and readable format.
- Don't add anything else to the output.
- Ensure you follow ALL these instructions when creating your output.
"""

# The URL for the OpenAI chat completions endpoint
url = "https://api.openai.com/v1/chat/completions"

# Headers including the Authorization token and Content-Type
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json",
}


def correct_text(input_text):
    # The data payload for the POST request
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": input_text},
        ],
        "temperature": 0,
        "max_tokens": 1024,
    }

    # Make the POST request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    # Read input from stdin for Alfred compatibility
    input_text = sys.argv[1].strip()

    if not input_text:
        print("No input provided.")
        sys.exit(1)

    corrected_text = correct_text(input_text)
    print(corrected_text)
