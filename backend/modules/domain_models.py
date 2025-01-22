from bson import ObjectId
from pydantic import BaseModel, Field


class Profile(BaseModel):
    id: str | None
    profile_img_url: str
    text: str

    @staticmethod
    def from_dict(id: str | ObjectId | None, data: dict):
        return Profile(
            id=str(id) if id else None,
            profile_img_url=data["profile_img_url"],
            text=data["text"]
        )


class Job(BaseModel):
    title: str
    start_date: date
    end_date: date | None
    duties: list[str]


class Resume(BaseModel):
    id: str | None
    full_name: str
    address_line_one: str
    address_line_two: str
    city: str
    state: str
    zip: int = Field(..., max=5)
    jobs: list[Job]
