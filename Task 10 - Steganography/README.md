<b>Exercise 10: Steganography</b>

<b> Design and write a steganography program: </b>

* With a graphical interface (web or desktop)

* That allows you to "hide" text using an image in any graphic format (hint: some are simpler than others)

* That allows you to "read" the text hidden in the picture (we assume the same scheme and algorithm)

* That allows you to encrypt the text with any algorithm (does not have to be your own, but it can)

<b>Worth to mention:</b>

[Source of the Steganography methods](https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2)

* All the images need to be in the png format.

* To use this program you need to manually put your png images into the /img/ directory. 

* Cipher and Decipher methods are copied from Task 05, but the emoji part is missing because
it was harder to encode emojis than the plaintext

* To simplify showing the image on the frontend I hardcoded the encrypted image name to hidden.png. 

<b>Installation</b>

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
   
5. Go to http://localhost:8080/ or use postman ([my postman requests collection](https://www.getpostman.com/collections/8cfddab1a272fc2a4ea0))
