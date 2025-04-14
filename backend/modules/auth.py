from hashlib import md5
from typing import Annotated

import bcrypt
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
import logging
import jwt

from config import CONFIG
from database import db
from modules.domain_models import User

router = APIRouter()
logger = logging.getLogger(__name__)


class AuthModel(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str


class DecodedJwt(BaseModel):
    sub: str
    iat: datetime
    exp: datetime
    user_id: str
    email: str
    first_name: str
    last_name: str
    roles: list[str]

    @staticmethod
    def from_dict(data: dict) -> "DecodedJwt":
        return DecodedJwt(
            sub=data["sub"],
            iat=data["iat"],
            exp=data["exp"],
            user_id=data["user_id"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            roles=data["roles"]
        )


Credentials = tuple[User, DecodedJwt, str]


class JWTBearer(HTTPBearer):
    required_roles: list | None = None

    def __init__(self, auto_error: bool = True, required_roles: list | None = None):
        self.required_roles = required_roles
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Credentials:
        bearer: HTTPAuthorizationCredentials | None = await super(JWTBearer, self).__call__(request)
        if bearer:
            if not bearer.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Bearer authorization not present or invalid.")

            credentials = JWTBearer.jwt_to_credentials(bearer.credentials)
            if not credentials:
                logger.info(f"Token {bearer.credentials} is invalid")
                raise HTTPException(status_code=401, detail="Access forbidden for token.")

            if JWTBearer.is_token_loggedout(bearer.credentials):
                logger.info(f"Token {bearer.credentials} is blacklisted")
                raise HTTPException(status_code=401, detail="Access forbidden for token.")

            if self.required_roles:
                user, _, _ = credentials
                for role in self.required_roles:
                    if role not in user.roles:
                        raise HTTPException(status_code=403, detail="Access forbidden for user.")

            return credentials
        else:
            raise HTTPException(status_code=401, detail="Access denied.")

    @staticmethod
    def is_token_loggedout(token: str):
        return db['token_blacklist'].find_one({"_id": md5(token.encode('utf-8')).hexdigest()}) is not None

    @staticmethod
    def blacklist_token(credentials: Credentials):
        db['token_blacklist'].insert_one({
            "_id": md5(credentials[2].encode('utf-8')).hexdigest(),
            "expire_at": credentials[1].exp
        })

    @staticmethod
    def jwt_to_credentials(jwtoken: str) -> Credentials | None:
        try:
            token = DecodedJwt.from_dict(jwt.decode(jwtoken, CONFIG.JWT_SECRET(), algorithms=["HS256"]))
            user_doc = db['users'].find_one({"_id": ObjectId(token.sub)})
            if not user_doc:
                return None
            doc: User = User.from_dict(user_doc["_id"], user_doc)
            if doc.active is not True:
                return None
            return (doc, token, jwtoken)
        except Exception as ex:
            return None


def build_token(user: User) -> str:
    payload_data = {
        # Standard headers
        "sub": user.id,
        "iat": datetime.now(),
        "exp": datetime.now() + timedelta(seconds=CONFIG.JWT_LIFETIME_S()),

        # Custom claims
        "user_id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "roles": user.roles
    }

    return jwt.encode(payload=payload_data, key=CONFIG.JWT_SECRET(), algorithm="HS256")


@router.post("/login")
def login(auth: AuthModel) -> LoginResponse:
    user_doc = db['users'].find_one({"email": auth.email.strip().lower()})
    if not user_doc:
        raise HTTPException(status_code=401, detail="Login failed")

    user = User.from_dict(user_doc["_id"], user_doc)
    if not bcrypt.checkpw(auth.password.encode("utf-8"), user.password_hash.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Login failed")

    return LoginResponse(token=build_token(user))


@router.post("/logout")
def logout(credentials: Annotated[Credentials, Depends(JWTBearer())]) -> Response:
    JWTBearer.blacklist_token(credentials)
    return Response(status_code=200)