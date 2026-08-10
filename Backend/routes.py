from fastapi import APIRouter
from menu import get_menu, find_meal
from chat import process_customer_message

router = APIRouter()

restaurants = []
orders = []


@router.get("/restaurants")
def get_restaurants():
    return restaurants


@router.post("/restaurants")
def add_restaurant(
    name: str,
    phone: str,
    location: str
):

    restaurant = {
        "id": len(restaurants) + 1,
        "name": name,
        "phone": phone,
        "location": location
    }

    restaurants.append(restaurant)

    return {
        "message": "Restaurant added successfully",
        "restaurant": restaurant
    }


@router.get("/menu")
def get_restaurant_menu():

    return {
        "restaurant": "Demo Restaurant",
        "menu": get_menu()
    }


@router.get("/menu/{meal_name}")
def get_meal(meal_name: str):

    meal = find_meal(meal_name)

    if meal is None:

        return {
            "found": False,
            "message": "Meal not found."
        }

    return {
        "found": True,
        "meal": meal
    }


@router.post("/chat")
def chat(message: str):

    return process_customer_message(message)


@router.get("/orders")
def get_orders():

    return orders


@router.post("/orders")
def create_order(
    customer: str,
    meal: str,
    quantity: int
):

    selected_meal = find_meal(meal)

    if selected_meal is None:

        return {
            "success": False,
            "message": "Sorry, that meal is not available."
        }

    order = {
        "id": len(orders) + 1,
        "customer": customer,
        "meal": selected_meal["name"],
        "quantity": quantity,
        "unit_price": selected_meal["price"],
        "total": selected_meal["price"] * quantity,
        "status": "Pending"
    }

    orders.append(order)

    return {
        "success": True,
        "message": "Order received successfully.",
        "order": order
    }
