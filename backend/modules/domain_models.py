from datetime import date
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

    @staticmethod
    def from_dict(id: str | ObjectId | None, data: dict):
        return Job(
            id=str(id) if id else None,
            title=data["start_date"],
            end_date=data["end_date"] if data["end_date"] else None,
            duties=data["duties"]
        )


class Resume(BaseModel):
    id: str | None
    full_name: str
    address_line_one: str
    address_line_two: str
    city: str
    state: str
    zip: int = Field(..., max=5)
    jobs: list[Job]

    @staticmethod
    def from_dict(id: str | ObjectId | None, data: dict):
        return Resume(
            id=str(id) if id else None,
            full_name=data["full_name"],
            address_line_one=data["address_line_one"],
            address_line_two=data["address_line_two"] if data["address_line_two"] else None,
            city=data["city"],
            state=data["state"],
            zip=data["zip"],
            jobs=data["jobs"]
        )


