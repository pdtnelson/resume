from fastapi import APIRouter
from modules.domain_models import Profile
router = APIRouter()


@router.get("/profile")
def get_profile():
    data = {"profile_img_url": "https://pdtnelson.com", "text": "Some text whoo!"}
    return Profile.from_dict(data)