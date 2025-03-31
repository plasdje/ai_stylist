from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.logic.item_logic import add_item

router = APIRouter()

class ItemRequest(BaseModel):
    user_id: str
    type: str
    category: str
    brand: str
    color: list = []
    material: str = None
    season: list = []
    style_tags: list = []
    image_url: str = None

@router.post("/items")
async def create_item(item_req: ItemRequest):
    try:
        
        data = item_req.model_dump(exclude={"user_id"})
        item = add_item(item_req.user_id, data)
        return {"message": "Item created successfully", "item_id": str(item.id)}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
