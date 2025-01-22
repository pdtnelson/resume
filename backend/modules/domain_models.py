from pydantic import BaseModel


class Profile(BaseModel):
    profile_img_url: str
    text: str

    @staticmethod
    def from_dict(data):
        return Profile(
            profile_img_url=data["profile_img_url"],
            text=data["text"]
        )
