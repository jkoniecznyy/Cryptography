import logging

from src.UserController import UserController

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    userController = UserController('crypto', 'users')

    username = input('Creating a user, please write the username')
    password1 = input('Please write the password')
    password2 = input('Please verify the password')
    if password1 == password2:
        try:
            userController.createUser(username, password1)
            print("Password successfully saved")
        except Exception as ex:
            logging.error(ex)
    else:
        logging.warning('Passwords dont match')
