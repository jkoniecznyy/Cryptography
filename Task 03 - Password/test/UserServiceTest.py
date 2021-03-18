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
        result = self.userService.addUserToDatabase('AddUsername1', 'password', 'salt')
        self.assertTrue(result)

    def testAddUserToDatabaseIsInDatabase(self):
        self.userService.addUserToDatabase('AddUsername2', 'password', 'salt')
        user = self.collection.find_one({"username": 'AddUsername2'})
        self.assertTrue(len(user))

    # TODO
    # def testAddUserToDatabaseThrowsException(self):
    #     self.assertRaises(Exception, self.userService.addUserToDatabase('', '', ''))

    def testFindUserByUsername(self):
        data = {'username': 'FindUsername', 'password': 'password', 'salt': 'salt'}
        self.collection.insert_one(data)
        user = self.userService.findUserByUsername('FindUsername')
        self.assertEqual(data, user)

    def testFindUserByUsernameThrowsException(self):
        self.assertRaises(Exception, self.userService.findUserByUsername('Voldemort'))
        # Harry, We Do Not Speak His Name  (⊙.⊙)


if __name__ == '__main__':
    unittest.main()
