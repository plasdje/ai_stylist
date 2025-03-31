from src.models.item_model import Item
from src.models.user_model import User

def add_item(user_id: str, data: dict) -> Item:
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise ValueError("User not found")
    
    
    item = Item(
        user=user,
        type=data.get("type"),
        category=data.get("category"),
        brand=data.get("brand"),
        color=data.get("color", []),
        material=data.get("material"),
        season=data.get("season", []),
        style_tags=data.get("style_tags", []),
        image_url=data.get("image_url")
    )
    item.save()
    return item
