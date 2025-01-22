import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from modules.domain_models import Profile
from database.db import db

router = APIRouter()


class CreateProfileRequest(BaseModel):
    profile_img_url: str
    text: str


@router.get("/profiles")
def get_profile():
    data = {"profile_img_url": "https://pdtnelson.com", "text": "Some text whoo!"}
    return Profile.from_dict(data)


@router.post("/profile")
def save_profile(profile: CreateProfileRequest):
    try:
        result = db['profiles'].insert_one(profile.model_dump())
        new_profile = Profile.from_dict(result.inserted_id, profile.model_dump())
        return new_profile
    except BaseException as ex:
        logging.exception(f"Error saving profile: {ex}")
        raise HTTPException(status_code=500, detail="Error creating profile")
