import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException


from database import db
from modules.domain_models import Resume, Job

router = APIRouter()


@router.get("/resumes/{_id}")
def get_resume(_id: str) -> Resume:
    doc = db["resumes"].find_one({"_id": ObjectId(_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    return Resume.from_dict(str("_id"), doc)


@router.post("/resumes")
def create_resume(resume: Resume) -> Resume:
    try:
        result = db['profiles'].insert_one(resume.model_dump())
        return Resume.from_dict(result.inserted_id, resume.model_dump())
    except BaseException as ex:
        logging.exception(f"Error saving profile: {ex}")
        raise HTTPException(status_code=500, detail="Error creating profile")