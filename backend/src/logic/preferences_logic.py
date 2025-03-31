from src.models.preferences_model import Preferences
from src.models.user_model import User

def create_preferences_for_user(user_id: str, data: dict) -> Preferences:

    user = User.objects(id=user_id).first()
    if not user:
        raise ValueError("User not found")

    prefs = Preferences(
        user=user,
        brands=data.get("brands", []),
        aesthetics=data.get("aesthetics", []),
        celebrities=data.get("celebrities", []),
        colors=data.get("colors", []),
    )
    prefs.save()
    
    user.preferences = prefs.id
    user.save()
    
    return prefs


def get_preferences(user_id: str):
    prefs = Preferences.objects(user=user_id).first()
    if not prefs:
        raise ValueError("Preferences not found for this user.")
    return prefs


def update_preferences(user_id: str, data: dict) -> Preferences:
    
    prefs = Preferences.objects(user=user_id).first()
    if not prefs:
        raise ValueError("Preferences not found for this user.")

    for field in ["brands", "aesthetics", "celebrities", "colors"]:
        if field in data:
            setattr(prefs, field, data[field])
    
    prefs.save()
    return prefs
