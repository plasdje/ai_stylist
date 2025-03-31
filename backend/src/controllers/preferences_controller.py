from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.utils.mongo_utils import document_to_dict

from src.logic.preferences_logic import (
    create_preferences_for_user,
    get_preferences,
    update_preferences
)

router = APIRouter()

class PreferencesRequest(BaseModel):
    brands: Optional[List[str]] = None
    aesthetics: Optional[List[str]] = None
    celebrities: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    occasion: Optional[List[str]] = None

@router.post("/preferences/{user_id}")
async def create_prefs(user_id: str, prefs_req: PreferencesRequest):

    try:
        data = prefs_req.model_dump(exclude_unset=True)
        prefs = create_preferences_for_user(user_id, data)
        return {"message": "Preferences created", "preferences_id": str(prefs.id)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/preferences/{user_id}")
async def read_prefs(user_id: str):
    try:
        prefs = get_preferences(user_id)
        return document_to_dict(prefs)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/preferences/{user_id}")
async def update_prefs(user_id: str, prefs_req: PreferencesRequest):
    try:
        data = prefs_req.model_dump(exclude_unset=True)
        updated = update_preferences(user_id, data)
        return {"message": "Preferences updated", "preferences": document_to_dict(updated)}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))