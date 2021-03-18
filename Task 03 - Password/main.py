import logging

from src.UserController import UserController

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    userController = UserController('crypto', 'users')
    logging.info('Creating a user, please write the username')
    username = input()
    logging.info('Please write the password')
    password1 = input()
    logging.info('Please verify the password')
    password2 = input()
    if password1 == password2:
        try:
            userController.createUser(username, password1)
            logging.info(userController.verifyPassword(username, password1))
            logging.info(userController.verifyPassword(username, password1+'x'))
        except Exception as ex:
            logging.warning(ex)
    else:
        logging.warning('Passwords dont match')
