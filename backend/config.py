import os


class CONFIG:

    @staticmethod
    def MONGO_CONN_STR():
        return os.getenv("MONGO_CONN_STR")

    @staticmethod
    def MONGO_DATABASE():
        return os.getenv("MONGO_DATABASE")

    @staticmethod
    def JWT_SECRET():
        return os.getenv("JWT_SECRET")

    @staticmethod
    def JWT_LIFETIME_S() -> int:
        expire_after_seconds = 30 * 24 * 60 * 60
        return int(os.getenv('JWT_LIFETIME_S', expire_after_seconds))