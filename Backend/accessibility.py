accessibility_profiles = {}


def create_profile(
    user_id: str,
    vision_assistance: bool = False,
    sign_language: bool = False,
    voice_assistance: bool = False,
    text_assistance: bool = True,
    language: str = "English"
):
    profile = {
        "user_id": user_id,
        "vision_assistance": vision_assistance,
        "sign_language": sign_language,
        "voice_assistance": voice_assistance,
        "text_assistance": text_assistance,
        "language": language
    }

    accessibility_profiles[user_id] = profile

    return profile


def get_profile(user_id: str):

    return accessibility_profiles.get(
        user_id,
        None
    )


def update_profile(
    user_id: str,
    **settings
):

    profile = accessibility_profiles.get(
        user_id
    )

    if profile is None:
        return None

    allowed_settings = [
        "vision_assistance",
        "sign_language",
        "voice_assistance",
        "text_assistance",
        "language"
    ]

    for key, value in settings.items():

        if key in allowed_settings:
            profile[key] = value

    return profile
