from typing import Optional, Dict
import pymongo
import logging


class UserService:

    def __init__(self, database: str, collection: str):
        """
            Connect to the database, raise Exception is something goes wrong
            :param database: name of the database to connect to
            :param collection: name of the collection to choose
        """
        try:
            self.client = pymongo.MongoClient()
            self.database = self.client[database]
            self.collection = self.database[collection]
        except Exception as ex:
            logging.error(ex)
            raise ex

    def addUserToDatabase(self, username: str, password: str, salt: str) -> bool:
        """
            Add a user to the database.
            :param username: username to be added to database
            :param password: already encrypted password to be added to database
            :param salt: salt to be added to database
            :return: True or False depending on success of the operation
        """
        data = {'username': username, 'password': password, 'salt': salt}
        try:
            self.collection.insert_one(data)
            return True
        except Exception as ex:
            logging.error(ex)
            return False

    def findUserByUsername(self, username: str) -> Optional[Dict]:
        """
            Find a user in the database.
            :param username: username to be found in database
            :return: Dictionary with user data or None depending on success of the operation
        """
        try:
            return self.collection.find_one({"username": username})
        except Exception as ex:
            logging.error(ex)
            return None
