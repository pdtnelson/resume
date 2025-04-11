import logging
import uuid

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from uuid import UUID

from modules.auth import JWTBearer
from modules.domain_models import Profile, PaginatedResponse, UserRole
from database import db

router = APIRouter()


class CreateProfileRequest(BaseModel):
    name: str
    job_title: str
    location: str
    salary: int
    profile_img_url: str
    text: str


@router.get("/profiles")
def get_profiles(limit: int = 10, offset: int = 0, tracking_uuid: str | None = None) -> PaginatedResponse[Profile]:
    try:
        if limit < 1 or limit > 100:
            raise HTTPException(status_code=422, detail="limit out of range")
        filter = {}

        if tracking_uuid is not None:
            filter["tracking_uuid"] = {"$eq": tracking_uuid}

        cursor = db["profiles"].find(filter)

        cursor.skip(offset)
        cursor.limit(limit)

        profiles = [Profile.from_dict(doc["_id"], doc) for doc in cursor]
        total = db["profiles"].count_documents(filter)

        return PaginatedResponse[Profile](data=profiles, total=total)
    except BaseException as ex:
        logging.exception(f"Failed to fetch profiles: {ex}")
        raise HTTPException(status_code=500, detail="Failed to fetch profiles")


@router.get("/profiles/{_id}")
def get_profile(_id: str) -> Profile:
    doc = db["profiles"].find_one({"_id": ObjectId(_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="profile not found")
    return Profile.from_dict(doc["_id"], doc)


@router.post("/profiles", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def create_profile(request: CreateProfileRequest) -> Profile:
    try:
        profile = Profile(
            id=None,
            tracking_uuid=str(uuid.uuid4()),
            name=request.name,
            job_title=request.job_title,
            location=request.location,
            salary=request.salary,
            profile_img_url=request.profile_img_url,
            text=request.text
        )
        result = db['profiles'].insert_one(profile.model_dump())
        return Profile.from_dict(result.inserted_id, profile.model_dump())
    except BaseException as ex:
        logging.exception(f"Error saving profile: {ex}")
        raise HTTPException(status_code=500, detail="Error creating profile")


@router.put("/profiles", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def update_profile(profile: Profile):
    try:
        doc = db["profiles"].find_one({"_id": ObjectId(profile.id)})
        if not doc:
            raise HTTPException(status_code=404, detail="Profile not found for update")

        db["profiles"].update_one({"_id": ObjectId(profile.id)}, {"$set": profile.model_dump(exclude="id")})
        updated = db["profiles"].find_one({"_id": ObjectId(profile.id)})
        return Profile.from_dict(updated["_id"], updated)
    except BaseException as ex:
        logging.exception(f"Error updating profile: {ex}")
        raise HTTPException(status_code=500, detail="Error updating profile")


@router.delete("/profiles/_id", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def delete_profile(_id: str):
    try:
        res = db["resumes"].delete_one({"_id": ObjectId(_id)})
        if res.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Profile not found")
    except HTTPException as ex:
        raise ex
    except BaseException as ex:
        logging.exception(f"Error deleting profile: {ex}")
        raise HTTPException(status_code=500, detail="Error deleting profile")
