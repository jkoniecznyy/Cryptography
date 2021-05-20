Exercise 04: FastAPI

Study the Cryptography library by repeating the examples from the lecture (symmetric encryption, public and private key generation, key serialization, etc.)

Create a simple API service with https://fastapi.tiangolo.com/ with endpoints:

a) symmetric:

GET symmetric / key -> returns a randomly generated symmetric key in the form of HEX (can be JSON)

POST symmetric / key -> sets the symmetric key in the form of HEX in request on the server

POST symmetric / encode -> we send the message, and as a result we get it encrypted

POST symmetric / decode -> we send the message, and as a result we get it decrypted

b) asymmetric:

GET asymmetric / key -> returns a new public and private key in HEX form (in JSON as dict) and sets it on the server

GET asymmetric / key / ssh -> returns public and private key in HEX format saved in OpenSSH format

POST asymmetric / key -> sets the public and private key in the form of HEX (in JSON as dict)

POST asymmetric / sign -> using the currently set private key, signs the message and returns it signed

POST asymmetric / verify -> using the currently set public key, verify that the message was encrypted with it

POST asymmetric / encode -> we send the message, and as a result we get it encrypted

POST asymmetric / decode -> we send the message, and as a result we get it decrypted


Take care of:
1. Transparency
2. Docstrings
3. Code quality and modularity
4. Error handling (e.g. someone gives a wrong value for the key, user-friendly information about the exception should be returned)
5. Verify the quality of documentation (it is generated automatically if you do docstrings well)

For volunteers:
1. Add unit tests to the project
2. Use jinja2 and make a simple frontend for that.

Setup:
```
pip install fastapi
pip install uvicorn
```

To run the API use following command:
```
uvicorn main:shared --reload
```
then go to http://127.0.0.1:8000/docs