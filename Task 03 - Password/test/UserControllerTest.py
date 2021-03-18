import logging
import unittest
import pymongo

from src.UserController import UserController


class UserControllerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = pymongo.MongoClient()
        cls.client.drop_database('cryptoTest')
        cls.database = cls.client['cryptoTest']
        cls.collection = cls.database['usersTest']

        cls.userController = UserController('cryptoTest', 'usersTest')

    def testCreateUser(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
