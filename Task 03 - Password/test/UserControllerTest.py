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

    def testCreateUserReturnTrue(self):
        result = self.userController.createUser('AddUsername1', 'password')
        self.assertTrue(result)

    def testCreateUserIsInDatabase(self):
        self.userController.createUser('AddUsername2', 'password')
        user = self.collection.find_one({"username": 'AddUsername2'})
        self.assertTrue(len(user))

    # TODO
    # def testCreateUserThrowsException(self):
    #     self.assertRaises(Exception, self.userService.addUserToDatabase('', '', ''))

    def testHashPassword(self):
        hashed = self.userController.hashPassword('black wand', b'dumbledore')
        self.assertEqual(hashed, 'd954c33266b8418a3e998cfd40dffee9b2c0a34260634d49e281e337160edec7')

    # TODO
    # def testHashPasswordException(self):
    #     self.assertRaises(Exception, self.userController.hashPassword('black wand', b'dumbledore'))

    def testVerifyPasswordTrue(self):
        self.assertTrue(self.userController.verifyPassword('AddUsername1', 'password'))

    def testVerifyPasswordFalse(self):
        self.assertFalse(self.userController.verifyPassword('AddUsername1', 'bonk'))

    # TODO
    # def testVerifyPasswordException(self):
    #     self.assertRaises(Exception,)


if __name__ == '__main__':
    unittest.main()
