# SignBridge translation foundation


SIGN_DICTIONARY = {
    "hello": {
        "text": "Hello",
        "description": "Greeting sign"
    },

    "thank_you": {
        "text": "Thank you",
        "description": "Thank-you sign"
    },

    "yes": {
        "text": "Yes",
        "description": "Agreement"
    },

    "no": {
        "text": "No",
        "description": "Disagreement"
    },

    "help": {
        "text": "Help",
        "description": "Request for assistance"
    },

    "food": {
        "text": "Food",
        "description": "Food-related sign"
    }
}


def sign_to_text(sign_name: str):

    sign_name = sign_name.lower().strip()

    sign = SIGN_DICTIONARY.get(sign_name)

    if sign is None:
        return {
            "success": False,
            "message": "Sign not recognised yet."
        }

    return {
        "success": True,
        "sign": sign_name,
        "text": sign["text"]
    }


def get_supported_signs():

    return list(SIGN_DICTIONARY.keys())
