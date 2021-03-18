import pymongo


class UserService:

    def __init__(self, database: str, collection: str):
        self.client = pymongo.MongoClient()
        self.database = self.client[database]
        self.collection = self.database[collection]

    def addUserToDatabase(self, username: str, password: str, salt: str):
        data = {'username': username, 'password': password, 'salt': salt}
        self.collection.insert_one(data)

    def findUserByUsername(self, username: str):
        return self.collection.find_one({"username": username})
