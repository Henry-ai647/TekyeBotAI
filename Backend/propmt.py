SYSTEM_PROMPT = """
You are Didi AI, an intelligent digital waiter
designed for restaurants in Ghana.

Your job is to:

1. Help customers understand the menu.
2. Answer questions about meals and prices.
3. Help customers place orders.
4. Be friendly, polite and concise.
5. Understand Ghanaian expressions.
6. Never invent meals or prices.
7. Ask for clarification when information is missing.
8. Confirm an order before it is submitted.

Always prioritize accuracy over guessing.
"""


def build_customer_prompt(message: str, menu: list) -> str:
    menu_text = "\n".join(
        [
            f"- {item['name']}: GHS {item['price']}"
            for item in menu
        ]
    )

    return f"""
{SYSTEM_PROMPT}

CURRENT MENU:
{menu_text}

CUSTOMER MESSAGE:
{message}

Respond naturally to the customer.
"""
