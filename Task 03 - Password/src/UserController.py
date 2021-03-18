import hashlib
import bcrypt
import logging

from src.UserService import UserService


class UserController:

    def __init__(self, database: str, collection: str):
        """ Create the userService object with provided database and collection names """

        self.userService = UserService(database, collection)

    def createUser(self, username: str, password: str) -> bool:
        """ Take username and password (both str),
            generate salt, get hashed password from the hashPassword function
            and then call userService.addUserToDatabase,
            return True or raise Exception """

        try:
            salt = bcrypt.gensalt()
            hashedPassword = self.hashPassword(password, salt)
            return self.userService.addUserToDatabase(username, hashedPassword, salt.decode("utf-8"))
        except Exception as ex:
            logging.warning(ex)
            raise ex

    @staticmethod
    def hashPassword(password: str, salt: bytes) -> str:
        """ Take password (str) and salt (bytes),
            hash the password,
            return hashedPassword (str) or raise Exception """

        try:
            bPassword = password.encode('utf-8')
            hashedPassword = hashlib.pbkdf2_hmac('sha256', bPassword, salt, 100000)
            return hashedPassword.hex()
        except Exception as ex:
            logging.warning(ex)
            raise ex

    def verifyPassword(self, username: str, password: str) -> bool:
        """ Take username (str) and password (str),
            call userService.findUserByUsername function,
            verify given password with the password stored in the database,
            return True / False or raise Exception """

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
