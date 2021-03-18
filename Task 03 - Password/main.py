import logging

from src.UserController import UserController

if __name__ == '__main__':
    userController = UserController('crypto', 'users')
    logging.warning('Creating a user, please write the username')
    username = input()
    logging.warning('Please write the password')
    password1 = input()
    logging.warning('Please verify the password')
    password2 = input()
    if password1 == password2:
        userController.createUser(username, password1)
    else:
        logging.warning('The passwords dont match')

    logging.warning(userController.verifyPassword(username, password1))
    logging.warning(userController.verifyPassword(username, password1+'x'))
