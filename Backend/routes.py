from fastapi import APIRouter

router = APIRouter()

restaurants = []

@router.get("/restaurants")
def get_restaurants():
    return restaurants

@router.post("/restaurants")
def add_restaurant(name: str, phone: str, location: str):

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

orders = []

@router.get("/orders")
def get_orders():
    return orders

@router.post("/orders")
def create_order(customer: str, meal: str, quantity: int):

    order = {
        "id": len(orders) + 1,
        "customer": customer,
        "meal": meal,
        "quantity": quantity,
        "status": "Pending"
    }

    orders.append(order)

    return {
        "message": "Order received",
        "order": order
    }
