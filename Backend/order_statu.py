VALID_STATUSES = [
    "Pending",
    "Preparing",
    "Ready",
    "Completed",
    "Cancelled"
]


def update_order_status(order, new_status):
    """
    Update the status of an order.
    """

    if new_status not in VALID_STATUSES:
        return {
            "success": False,
            "message": "Invalid order status."
        }

    order["status"] = new_status

    return {
        "success": True,
        "message": f"Order status updated to {new_status}.",
        "order": order
    }


def get_valid_statuses():
    return VALID_STATUSES
