import random

from faker import Faker

from modules.domain_models import Profile

fake = Faker()


def create_profile(name: str | None = None):
    return Profile(
        name=name if name else fake.company(),
        job_title=fake.job_male(),
        location=fake.city(),
        salary=random.randint(85000, 250000),
        profile_img_url="https://placecats.com/300/400",
        text="".join(fake.paragraphs(nb=3))
    )