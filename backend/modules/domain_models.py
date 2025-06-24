from enum import StrEnum
from uuid import UUID
from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr


class PaginatedResponse[T](BaseModel):
    data: list[T]
    total: int


class Profile(BaseModel):
    id: str | None = None
    tracking_uuid: str
    name: str
    job_title: str
    location: str
    salary: int
    profile_img_url: str
    text: str

    @staticmethod
    def from_dict(id: str | ObjectId | None, data: dict):
        return Profile(
            id=str(id) if id else None,
            tracking_uuid=data["tracking_uuid"],
            name=data["name"],
            job_title=data["job_title"],
            location=data["location"],
            salary=data["salary"],
            profile_img_url=data["profile_img_url"],
            text=data["text"]
        )


class Job(BaseModel):
    title: str
    company: str
    company_logo_url: str | None = None
    start_date: datetime
    end_date: datetime | None = None
    description: str

    @staticmethod
    def from_dict(data: dict):
        return Job(
            title=data["title"],
            company=data["company"],
            company_log_url=data["company_logo_url"] if data["company_logo_url"] else None,
            start_date=data["start_date"],
            end_date=data["end_date"] if data["end_date"] else None,
            description=data["duties"]
        )


class Education(BaseModel):
    school: str
    city: str
    state: str
    description: str


class Certification(BaseModel):
    name: str
    issuer: str
    certification_url: str | None


class Resume(BaseModel):
    id: str | None = None
    full_name: str
    address_line_one: str
    address_line_two: str | None
    city: str
    state: str
    zip: int = Field(..., max=5)
    skills: list[str]
    jobs: list[Job]
    education: list[Education]
    certifications: list[Certification] | None
    revision: int  # PDT: Start at zero and reserve zero as current

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
            skills=data["skills"],
            jobs=data["jobs"],
            education=data["education"],
            certifications=data["certifications"] if data["certifications"] else None,
            revision=data["revision"]
        )


class UserRole(StrEnum):
    SITE_ADMIN = "SITE_ADMIN"


class User(BaseModel):
    id: str | None = None
    active: bool
    first_name: str
    last_name: str
    email: EmailStr
    password_hash: str = Field(..., exclude=True)
    roles: list[UserRole]
    created_at: datetime

    @staticmethod
    def from_dict(id: str | ObjectId, data: dict) -> "User":
        return User(
            id=str(id) if id else None,
            active=data["active"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            password_hash=data["password_hash"],
            roles=data["roles"],
            created_at=data["created_at"]
        )
