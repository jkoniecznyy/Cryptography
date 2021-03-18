import hashlib
import bcrypt
import logging
from typing import Optional, Union

from src.UserService import UserService


class UserController:

    def __init__(self, database: str, collection: str):
        self.userService = UserService(database, collection)

    def createUser(self, username: str, password: str) -> bool:
        try:
            salt = bcrypt.gensalt()
            hashedPassword = self.hashPassword(password, salt)
            return self.userService.addUserToDatabase(username, hashedPassword, salt.decode("utf-8"))
        except Exception as ex:
            logging.warning(ex)
            raise ex

    @staticmethod
    def hashPassword(password: str, salt: bytes) -> Optional[str]:
        try:
            bPassword = password.encode('utf-8')
            hashedPassword = hashlib.pbkdf2_hmac('sha256', bPassword, salt, 100000)
            return hashedPassword.hex()
        except Exception as ex:
            logging.warning(ex)
            raise ex

    def verifyPassword(self, username: str, password: str) -> Union[bool, Exception]:
        try:
            user = self.userService.findUserByUsername(username)
            salt = user['salt'].encode('utf-8')
            hashedPassword = self.hashPassword(password, salt)
            if hashedPassword == user['password']:
                return True
            return False
        except Exception as ex:
            logging.warning(ex)
            raise ex
