def create_order_summary(
    customer: str,
    meal: str,
    quantity: int,
    price: float
):
    total = quantity * price

    return {
        "customer": customer,
        "meal": meal,
        "quantity": quantity,
        "unit_price": price,
        "total": total,
        "status": "Awaiting Confirmation"
    }


def confirm_order(order):
    order["status"] = "Confirmed"

    return {
        "success": True,
        "message": "Order confirmed successfully.",
        "order": order
    }
