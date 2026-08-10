from ai import ask_gemma
from menu import get_menu
from prompts import build_customer_prompt


def process_customer_message(message: str):
    """
    Process a customer's message using Didi AI.
    """

    menu = get_menu()

    prompt = build_customer_prompt(
        message=message,
        menu=menu
    )

    response = ask_gemma(prompt)

    return {
        "customer_message": message,
        "ai_response": response
    }
