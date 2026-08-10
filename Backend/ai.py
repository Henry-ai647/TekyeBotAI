import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3"


def ask_gemma(prompt: str) -> str:
    """
    Send a prompt to Gemma running through Ollama.
    """

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Sorry, I couldn't generate a response."
        )

    except requests.exceptions.RequestException:
        return (
            "AI is currently offline. "
            "Please try again later."
        )
