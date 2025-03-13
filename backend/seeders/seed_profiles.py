from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / "../.env")
from database import db
from factories import profile_factory
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    profiles = db["profiles"]
    logger.info("Dropping profiles")
    profiles.drop()
    logger.info("Seeding profiles")
    profiles.insert_one(profile_factory.create_profile("default").model_dump(exclude="id"))
    for n in range(6):
        profiles.insert_one(profile_factory.create_profile().model_dump(exclude="id"))
    logger.info("Profile seeding complete")
