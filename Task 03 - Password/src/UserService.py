import pymongo
import logging


class UserService:

    def __init__(self, database: str, collection: str):
        """ Take database and collection names (both str),
            connect to the database,
            raise Exception is something goes wrong """
        try:
            self.client = pymongo.MongoClient()
            self.database = self.client[database]
            self.collection = self.database[collection]
        except Exception as ex:
            logging.warning(ex)
            raise ex

    def addUserToDatabase(self, username: str, password: str, salt: str) -> bool:
        """ Take username, password and salt (all str),
            put them into to database,
            return True or raise Exception """
        data = {'username': username, 'password': password, 'salt': salt}
        try:
            self.collection.insert_one(data)
            return True
        except Exception as ex:
            logging.warning(ex)
            raise ex

    def findUserByUsername(self, username: str):
        """ Take username (str),
            look for the user in database,
            return the user or raise Exception """
        try:
            return self.collection.find_one({"username": username})
        except Exception as ex:
            logging.warning(ex)
            raise ex
