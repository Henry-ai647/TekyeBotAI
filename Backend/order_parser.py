import re

from menu import get_menu
from order_manager import create_order_summary


def detect_quantity(message: str) -> int:
    """
    Try to find a quantity in the customer's message.
    """

    match = re.search(r"\b(\d+)\b", message)

    if match:
        quantity = int(match.group(1))

        if quantity > 0:
            return quantity

    return 1


def detect_meal(message: str):
    """
    Find a menu item mentioned in the customer's message.
    """

    message = message.lower()

    for item in get_menu():

        meal_name = item["name"].lower()

        if meal_name in message:
            return item

    return None


def prepare_order(customer: str, message: str):

    meal = detect_meal(message)

    if meal is None:
        return {
            "success": False,
            "message": (
                "I couldn't identify the meal. "
                "Please tell me which meal you want."
            )
        }

    quantity = detect_quantity(message)

    order = create_order_summary(
        customer=customer,
        meal=meal["name"],
        quantity=quantity,
        price=meal["price"]
    )

    return {
        "success": True,
        "message": "Please confirm your order.",
        "order": order
    }
