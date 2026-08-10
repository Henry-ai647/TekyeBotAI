from fastapi import APIRouter
from menu import get_menu, find_meal
from chat import from order_manager import create_order_summary, from customer import add_customer, get_customers, find_customer
router = from whatsapp import receive_whatsapp_message
from order_parser import from order_status import update_order_status, get_valid_statuses
restaurants = []
from notifications import (
    create_notification,
    get_notifications,
    from accessibility import (
    create_profile,
    get_profile,
    update_profile
)


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
@router.post("/orders/preview")
def preview_order(
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

    order = create_order_summary(
        customer=customer,
        meal=selected_meal["name"],
        quantity=quantity,
        price=selected_meal["price"]
    )

    return {
        "success": True,
        "message": "Please confirm your order.",
        "order": order
    }


@router.post("/orders/confirm")
def confirm_customer_order(
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

    order = create_order_summary(
        customer=customer,
        meal=selected_meal["name"],
        quantity=quantity,
        price=selected_meal["price"]
    )

    return confirm_order(order)
    
@router.post("/customers")
def create_customer(
    name: str,
    phone: str
):

    existing_customer = find_customer(phone)

    if existing_customer:
        return {
            "success": True,
            "message": "Customer already exists.",
            "customer": existing_customer
        }

    customer = add_customer(
        name=name,
        phone=phone
    )

    return {
        "success": True,
        "message": "Customer registered successfully.",
        "customer": customer
    }


@router.get("/customers")
def customers():

    return {
        "customers": @router.post("/whatsapp/message")
def whatsapp_message(
    sender: str,
    message: str
):

    result = receive_whatsapp_message(
        sender=sender,
        message=message
    )

    return {
        "success": True,
        "whatsapp": @router.post("/orders/understand")
def understand_order(
    customer: str,
    message: str
):

    return prepare_order(
        customer=customer,
        message=@router.get("/orders/statuses")
def order_statuses():

    return {
        "statuses": get_valid_statuses()
    }


@router.put("/orders/{order_id}/status")
def change_order_status(
    order_id: int,
    status: str
):

    for order in orders:

        if order["id"] == order_id:

            return update_order_status(
                order,
                status
            )

    return {
        "success": False,
        "message": "Order not @router.get("/notifications")
def notifications():

    return {
        "notifications": get_notifications()
    }


@router.put("/notifications/{notification_id}/read")
def read_notification(notification_id: int):

    return mark_notification_read(
        @router.post("/accessibility/profile")
def create_accessibility_profile(
    user_id: str,
    vision_assistance: bool = False,
    sign_language: bool = False,
    voice_assistance: bool = False,
    text_assistance: bool = True,
    language: str = "English"
):

    profile = create_profile(
        user_id=user_id,
        vision_assistance=vision_assistance,
        sign_language=sign_language,
        voice_assistance=voice_assistance,
        text_assistance=text_assistance,
        language=language
    )

    return {
        "success": True,
        "profile": profile
    }


@router.get("/accessibility/profile/{user_id}")
def get_accessibility_profile(user_id: str):

    profile = get_profile(user_id)

    if profile is None:
        return {
            "success": False,
            "message": "Accessibility profile not found."
        }

    return {
        "success": True,
        "profile": profile
    }
