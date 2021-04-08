from fastapi import FastAPI
from src.Asymmetric import Asymmetric
from src.Symmetric import Symmetric
from typing import Optional

shared = FastAPI()
symmetric = Symmetric()
asymmetric = Asymmetric()


# Symmetric routes
@shared.get("/symmetric/key/")
def getSymmetricKey():
    """
        Return a randomly generated symmetric key in the form of HEX
        :rtype: Optional[hex]
    """
    return symmetric.generateKey()


@shared.post("/symmetric/key/")
def postSymmetricKey(key: str) -> bool:
    """
        Set the public and private key on the server in the form of HEX
        (in JSON as dict)
        :rtype: bool
    """
    return symmetric.setKey(key)


@shared.post("/symmetric/encode/")
def postSymmetricEncode(text: str) -> Optional[bytes]:
    """
        Send a message, and return it encrypted
        :rtype: Optional[bytes]
    """
    return symmetric.encode(text)


@shared.post("/symmetric/decode/")
def postSymmetricDecode(text: bytes) -> Optional[bytes]:
    """
        Set the symmetric key provided in the form of HEX in request on the server
        :rtype: Optional[bytes]
    """
    return symmetric.decode(text)


# Asymmetric routes
@shared.get("/asymmetric/key/")
def getAsymmetricKey():
    """
        Return a new public and private key in the form of HEX
        (in JSON as dict) and set it on the server
    """
    privateKey, publicKey = asymmetric.generateKeys()
    asymmetric.setKeys(privateKey, publicKey)
    return asymmetric.getKeysInHex()


@shared.get("/asymmetric/key/ssh")
def getAsymmetricKeySSH():
    """
        Return public and private key in HEX format
        saved in OpenSSH format
    """
    return asymmetric.getKeysInSSH()


@shared.post("/asymmetric/key/")
def postAsymmetricKey(privateKey, publicKey):
    """
        Set the public and private key on the server in the form of HEX
        (in JSON as dict)
    """
    return asymmetric.setKeys(privateKey, publicKey)


@shared.post("/asymmetric/sign/")
def postSignMessage(message: str):
    """
        Use the currently set private key,
        sign the message and return it with the signed one
    """
    return asymmetric.sign(message)


@shared.post("/asymmetric/verify/")
def postVerifyMessage(message, signature):
    """
        Use the currently set public key,
        verify that the message was encrypted with it
    """
    return asymmetric.verify(message, signature)


@shared.post("/asymmetric/encode/")
def postEncode(message):
    """
        Send a message, and return it encrypted
    """
    return asymmetric.encrypt(message)


@shared.post("/asymmetric/decode/")
def postDecode(message):
    """
        Send the message, and return it decrypted
    """
    return asymmetric.decode(message)
