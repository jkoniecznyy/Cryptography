Exercise 3: Writing Passwords, hash functions continued

1. Design and implement your own simple way of storing passwords in the database, e.g. sqlite (I used MongoDB): 
   the user enters the password twice, you randomize the salt, hash everything and save the hash and salt to the database. 
   Add a password verification function.

2. Redo point 1 by using pbkdf2_hmac. Make a decent project out of it (tests, docstrings, etc.)