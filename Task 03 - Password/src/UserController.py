import hashlib
import logging
from src.UserService import UserService


class UserController:

    def __init__(self, database: str, collection: str):
        us = UserService(database, collection)

    @staticmethod
    def createUser(username: bytes, password: bytes):
        salt = b'adsa'
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
        logging.warning(dk.hex())
