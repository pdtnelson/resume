import logging
import os
from pymongo import MongoClient
from config import CONFIG

logger = logging.getLogger(__name__)

assert CONFIG.MONGO_CONN_STR() is not None, "MONGO_CONNECTION_STR must be set"
assert CONFIG.MONGO_DATABASE() is not None, "MONGO_DATABASE must be set"

mongo = MongoClient(os.getenv("MONGO_CONN_STR"))
try:
    mongo.admin.command("ping")
    logger.info("Database connected")
except Exception as e:
    logger.error(e)
    mongo = None
    exit(-1337)

db = mongo[CONFIG.MONGO_DATABASE()]
