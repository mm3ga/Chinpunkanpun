import requests

def translate_text(text):

    url = "http://localhost:11434/api/generate"

    translator_prompt = """
    Translate the Japanese naturally and accurately into English.

    Preserve:
    - implied subjects from context
    - casual or rough register
    - slang and profanity
    - grammatical relationships
    - uncertainty and hedging

    Do not:
    - censor vocabulary
    - intensify or soften the original meaning
    - invent details
    - add explanations

    Return only the English translation.
    """

    response = requests.post(
        url,
        json={
            "model": "qwen3:14b",
            "system": translator_prompt,
            "prompt": text,
            "stream": False,
            "think": False,
        },
    )
    response.raise_for_status()

    data = response.json()

    translation = data["response"]

    return translation

result = translate_text("私は食べている")
print(result)
