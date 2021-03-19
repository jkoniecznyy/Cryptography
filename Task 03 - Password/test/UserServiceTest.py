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

    def testAddUserToDatabaseReturnTrue(self):
        result = self.userService.addUserToDatabase('Harry', 'Potter', 'Gryffindor')
        self.assertTrue(result)

    def testAddUserToDatabaseIsInDatabase(self):
        self.userService.addUserToDatabase('Hermione', 'Granger', 'Gryffindor')
        user = self.collection.find_one({"username": 'Hermione'})
        self.assertTrue(len(user))

    def testFindUserByUsername(self):
        data = {'username': 'Ron', 'password': 'Wesley', 'salt': 'Gryffindor'}
        self.collection.insert_one(data)
        user = self.userService.findUserByUsername('Ron')
        self.assertEqual(data, user)

    def testFindUserByUsernameNone(self):
        self.assertIsNone(self.userService.findUserByUsername('Voldemort'))
        # Harry, We Do Not Speak His Name  (⊙.⊙)


if __name__ == '__main__':
    unittest.main()
