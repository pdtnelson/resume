from datetime import datetime

from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).parent / "../.env")

from database import db
import logging
from modules.domain_models import User, UserRole


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    users = db["users"]
    logger.info("Dropping Users")
    users.drop()
    logger.info("Seeding users")

    user = User(
        active=True,
        email="peter@pdtnelson.com",
        first_name="Peter",
        last_name="Nelson",
        password_hash="$2b$12$Lw0WkcpqhX/ij9otO5CH/easveEH4j1/TOX6myJ509z25Xd.jd0Ju",
        roles=[UserRole.SITE_ADMIN],
        created_at=datetime.now(),
    )

    users.insert_one({"password_hash": user.password_hash, **user.model_dump(exclude={"id"})})

    logger.info("Seeding user complete")