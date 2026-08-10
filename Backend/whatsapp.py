from chat import process_customer_message


def receive_whatsapp_message(
    sender: str,
    message: str
):
    """
    Process an incoming WhatsApp message.
    """

    ai_result = process_customer_message(message)

    return {
        "sender": sender,
        "message": message,
        "reply": ai_result["ai_response"]
    }


def format_whatsapp_reply(message: str):
    """
    Prepare a response to send back to WhatsApp.
    """

    return {
        "messaging_product": "whatsapp",
        "text": {
            "body": message
        }
    }
