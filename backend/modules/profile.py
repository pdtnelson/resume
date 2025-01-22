import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from modules.domain_models import Profile
from database import db

router = APIRouter()


class CreateProfileRequest(BaseModel):
    profile_img_url: str
    text: str


@router.get("/profiles/{_id}")
def get_profile(_id: str) -> Profile:
    doc = db["profiles"].find_one({"_id": ObjectId(_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="profile not found")
    return Profile.from_dict(doc["_id"], doc)


@router.post("/profiles")
def create_profile(profile: Profile) -> Profile:
    try:
        result = db['profiles'].insert_one(profile.model_dump())
        return Profile.from_dict(result.inserted_id, profile.model_dump())
    except BaseException as ex:
        logging.exception(f"Error saving profile: {ex}")
        raise HTTPException(status_code=500, detail="Error creating profile")
