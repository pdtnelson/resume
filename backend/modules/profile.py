import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from modules.domain_models import Profile, PaginatedResponse
from database import db

router = APIRouter()


class CreateProfileRequest(BaseModel):
    profile_img_url: str
    text: str


@router.get("/profiles")
def get_profiles(limit: int = 10, offset: int = 0) -> PaginatedResponse[Profile]:
    try:
        if limit < 1 or limit > 100:
            raise HTTPException(status_code=422, detail="limit out of range")
        cursor = db["profiles"].find()
        cursor.skip(offset)
        profiles = [Profile.from_dict(doc["_id"], doc) for doc in cursor.limit(limit)]
        total = db["profiles"].count_documents({})
        return PaginatedResponse[Profile](data=profiles, total=total)
    except BaseException as ex:
        logging.exception(f"Failed to fetch profiles")
        raise HTTPException(status_code=500, detail="Failed to fetch profiles")

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
