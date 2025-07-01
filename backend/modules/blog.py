import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.responses import Response

from database import db
from modules.auth import JWTBearer
from modules.domain_models import PaginatedResponse, BlogPost, UserRole

router = APIRouter()


@router.get("/posts")
def get_all_posts(limit: int = 10, offset: int = 0) -> PaginatedResponse[BlogPost]:
    cursor = db["blog_posts"].find({})

    cursor.skip(offset)
    cursor.limit(limit)

    data = [BlogPost.from_dict(doc["_id"], doc) for doc in cursor]
    total = db["blog_posts"].count_documents({})

    return PaginatedResponse(data=data, total=total)


@router.get("/posts/{_id}")
def get_blog_post(_id: str) -> BlogPost | Response:
    try:
        doc = db["blog_posts"].find({"_id": {"$eq": _id}})
        if not doc:
            return Response("Blog post not found", status_code=404)
        return BlogPost.from_dict(doc["_id"], doc)
    except Exception as ex:
        logging.exception(f"Error fetching blog post {_id}:")
        raise HTTPException(status_code=500, detail="Error getting blog post")


@router.post("/posts", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def create_post(blog_post: BlogPost) -> BlogPost:
    try:
        result = db["blog_posts"].insert_one(blog_post.model_dump(exclude="id"))
        return BlogPost.from_dict(result.inserted_id, blog_post.model_dump())
    except Exception:
        logging.exception(f"Error creating blog post:")
        raise HTTPException(status_code=500, detail="Error creating blog post")


@router.put("/posts", dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def update_post(blog_post: BlogPost) -> BlogPost | Response:
    try:
        doc = db["blog_posts"].find_one({"_id": {"$eq": blog_post.id}})
        if not doc:
            return Response("Resume not found for update", status_code=404)
        db["blog_posts"].update_one({"_id", {"$set": blog_post.model_dump(exclude="id")}})
        updated = db["blog_posts"].find_one({"_id": {"$eq": blog_post.id}})
        return BlogPost.from_dict(updated["_id"], updated)
    except Exception:
        logging.exception(f"Error updating post")
        raise HTTPException(status_code=500, detail="Error updating post")


@router.delete("/posts/{_id}", status_code=status.HTTP_204_NO_CONTENT,  dependencies=[
    Depends(JWTBearer(required_roles=[UserRole.SITE_ADMIN]))
])
def delete_post(_id: str) -> Response:
    try:
        result = db["blog_posts"].delete_one({"_id": ObjectId(_id)})
        if result.deleted_count == 0:
            return Response("Post not found", status_code=404)
    except Exception:
        logging.exception(f"Error deleting post {id}")
        raise HTTPException(status_code=500, detail="Error deleting post")
