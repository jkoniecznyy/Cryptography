import logging
import unittest
import pymongo

from src.UserService import UserService


class UserControllerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = pymongo.MongoClient()
        cls.client.drop_database('cryptoTest')
        cls.database = cls.client['cryptoTest']
        cls.collection = cls.database['usersTest']

        cls.userService = UserService('cryptoTest', 'usersTest')

    def testAddUserToDatabase(self):
        self.userService.addUserToDatabase('AddUsername', 'password', 'salt')
        user = self.collection.find_one({"username": 'AddUsername'})
        self.assertTrue(len(user))

    def testFindUserByUsername(self):
        data = {'username': 'FindUsername', 'password': 'password', 'salt': 'salt'}
        self.collection.insert_one(data)
        user = self.userService.findUserByUsername('FindUsername')
        self.assertEqual(data, user)


if __name__ == '__main__':
    unittest.main()
