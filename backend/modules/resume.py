import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException


from database import db
from modules.domain_models import Resume, Job, PaginatedResponse

router = APIRouter()


# TODO: Versioning (Add query param to get latest, implement revision field)
@router.get("/resumes")
def get_resume(limit: int = 10, offset: int = 0) -> PaginatedResponse[Resume]:
    cursor = db['resumes'].find({})

    cursor.skip(offset)
    cursor.limit(limit)

    data = [Resume.from_dict(doc.id, doc) for doc in cursor]
    total = db['resumes'].count_documents({})

    return PaginatedResponse(data=data, total=total)


@router.post("/resumes")
def create_resume(resume: Resume) -> Resume:
    try:
        result = db['resumes'].insert_one(resume.model_dump(exclude="id"))
        return Resume.from_dict(result.inserted_id, resume.model_dump())
    except BaseException as ex:
        logging.exception(f"Error saving profile: {ex}")
        raise HTTPException(status_code=500, detail="Error creating profile")