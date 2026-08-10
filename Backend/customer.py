customers = []


def add_customer(name: str, phone: str):
    customer = {
        "id": len(customers) + 1,
        "name": name,
        "phone": phone
    }

    customers.append(customer)

    return customer


def get_customers():
    return customers


def find_customer(phone: str):
    for customer in customers:
        if customer["phone"] == phone:
            return customer

    return None
