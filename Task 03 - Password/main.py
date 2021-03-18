from src.UserController import UserController

if __name__ == '__main__':
    uc = UserController('crypto', 'users')
    uc.createUser(b'test', b'test')
