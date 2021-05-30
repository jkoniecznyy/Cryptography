Exercise 10: Steganography

Design and write a steganography program:

with a graphical interface (web or desktop)

that allows you to "hide" text using an image in any graphic format (hint: some are simpler than others)

that allows you to "read" the text hidden in the picture (we assume the same scheme and algorithm)

that allows you to encrypt the text with any algorithm (does not have to be your own, but it can)


[Source of the Steganography class](https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2)

[Cipher and Decipher classes are copied from Task 05](https://github.com/jkoniecznyy/Cryptography/tree/main/Task%2005%20-%20Cryptoanalysis)


Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install backend.
```
$ pip install pipenv 
$ pipenv install 
``` 
3. Install frontend
```
cd frontend/
npm install
```
4. Run backend and frontend in two separate consoles:
    * `/Task 10 - Steganography/> pipenv run python main.py` 
    * `/Task 10 - Steganography/frontend> npm run serve`
   
5. Use postman or go to http://localhost:8080/