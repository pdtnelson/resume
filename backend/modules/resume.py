import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status, Depends

from database import db
from modules.auth import JWTBearer
from modules.domain_models import Resume, Job, PaginatedResponse, UserRole

router = APIRouter()


# TODO: Versioning (Add query param to get latest, implement revision field)
@router.get("/resumes")
def get_resume(limit: int = 10, offset: int = 0) -> PaginatedResponse[Resume]:
    cursor = db['resumes'].find({})

    cursor.skip(offset)
    cursor.limit(limit)

    data = [Resume.from_dict(doc["_id"], doc) for doc in cursor]
    total = db['resumes'].count_documents({})

    return PaginatedResponse(data=data, total=total)


@router.post("/resumes", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def create_resume(resume: Resume) -> Resume:
    try:
        result = db['resumes'].insert_one(resume.model_dump(exclude="id"))
        return Resume.from_dict(result.inserted_id, resume.model_dump())
    except BaseException as ex:
        logging.exception(f"Error saving resume: {ex}")
        raise HTTPException(status_code=500, detail="Error creating resume")


@router.put("/resumes", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def update_resume(resume: Resume):
    try:
        doc = db["resumes"].find_one({"_id": ObjectId(resume.id)})
        if not doc:
            raise HTTPException(status_code=404, detail="Resume not found for update")

        db["resumes"].update_one({"_id": ObjectId(resume.id)}, {"$set": resume.model_dump(exclude="id")})
        updated = db["resumes"].find_one({"_id": ObjectId(resume.id)})
        return Resume.from_dict(updated["_id"], updated)
    except BaseException as ex:
        logging.exception(f"Error updating resume: {ex}")
        raise HTTPException(status_code=500, detail="Error updating resume")


@router.delete("/resumes/{_id}", status_code=status.HTTP_204_NO_CONTENT,  dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def delete_resume(_id: str):
    try:
        res = db["resumes"].delete_one({"_id": ObjectId(_id)})
        if res.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Resume not found")
    except HTTPException as ex:
        raise ex
    except BaseException as ex:
        logging.exception(f"Error deleting resume: {ex}")
        raise HTTPException(status_code=500, detail="Error deleting resume")