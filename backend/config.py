import os


class CONFIG:

    @staticmethod
    def MONGO_CONN_STR():
        return os.getenv('MONGO_CONN_STR')

    @staticmethod
    def MONGO_DATABASE():
        return os.getenv('MONGO_DATABASE')