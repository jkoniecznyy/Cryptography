import hashlib
import bcrypt
import logging

from src.UserService import UserService


class UserController:

    def __init__(self, database: str, collection: str):
        """
            Create the UserService object with provided data or raise Exception
            :param database: name of the database to connect to
            :param collection: name of the collection to choose
        """
        try:
            self.userService = UserService(database, collection)
        except Exception as ex:
            logging.error(ex)
            raise ex

    def createUser(self, username: str, password: str) -> bool:
        """
            Generate salt, call hashPassword function,
            call UserService.addUserToDatabase function,
            :param username: username to be added to database
            :param password: cleartext password to be added to database
            :return: True or False depending on success of the operation
        """
        try:
            salt = bcrypt.gensalt()
            hashedPassword = self.hashPassword(password, salt)
            return self.userService.addUserToDatabase(username, hashedPassword, salt.decode("utf-8"))
        except Exception as ex:
            logging.error(ex)
            return False

    @staticmethod
    def hashPassword(password: str, salt: bytes) -> str:
        """
            Hash the password or raise Exception
            :param password: cleartext password to be hashed
            :param salt: salt to be used in hashing
            :return: hashedPassword
        """
        try:
            bPassword = password.encode('utf-8')
            hashedPassword = hashlib.pbkdf2_hmac('sha256', bPassword, salt, 100000)
            return hashedPassword.hex()
        except Exception as ex:
            logging.error(ex)
            raise ex

    def verifyPassword(self, username: str, password: str) -> bool:
        """
            Call UserService.findUserByUsername function,
            hash and verify given password with the password stored in the database
            :param username: username to be found in database
            :param password: plaintext password
            :return: True or False depending on success of the operation
        """
        user = self.userService.findUserByUsername(username)
        if user:
            try:
                salt = user['salt'].encode('utf-8')
                hashedPassword = self.hashPassword(password, salt)
                if hashedPassword == user['password']:
                    return True
            except Exception as ex:
                logging.error(ex)
        return False
