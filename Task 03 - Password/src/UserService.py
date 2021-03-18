import pymongo
import logging


class UserService:

    def __init__(self, database: str, collection: str):
        try:
            self.client = pymongo.MongoClient()
            self.database = self.client[database]
            self.collection = self.database[collection]
        except Exception as ex:
            logging.warning(ex)
            raise ex

    def addUserToDatabase(self, username: str, password: str, salt: str) -> bool:
        data = {'username': username, 'password': password, 'salt': salt}
        try:
            self.collection.insert_one(data)
            return True
        except Exception as ex:
            logging.warning(ex)
            raise ex

    def findUserByUsername(self, username: str):
        try:
            return self.collection.find_one({"username": username})
        except Exception as ex:
            logging.warning(ex)
            raise ex
