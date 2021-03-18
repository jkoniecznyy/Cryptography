import hashlib
import bcrypt

from src.UserService import UserService


class UserController:

    def __init__(self, database: str, collection: str):
        self.userService = UserService(database, collection)

    def createUser(self, username: str, password: str):
        salt = bcrypt.gensalt()
        hashedPassword = self.hashPassword(password, salt)
        self.userService.addUserToDatabase(username, hashedPassword, salt.decode("utf-8"))

    @staticmethod
    def hashPassword(password: str, salt: bytes) -> str:
        bPassword = password.encode('utf-8')
        hashedPassword = hashlib.pbkdf2_hmac('sha256', bPassword, salt, 100000)
        return hashedPassword.hex()

    def verifyPassword(self, username: str, password: str) -> bool:
        user = self.userService.findUserByUsername(username)
        salt = user['salt'].encode('utf-8')
        hashedPassword = self.hashPassword(password, salt)
        if hashedPassword == user['password']:
            return True
        return False
