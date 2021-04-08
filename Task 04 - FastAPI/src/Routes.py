from fastapi import FastAPI
from src.Asymmetric import Asymmetric
from src.Symmetric import Symmetric
from typing import Optional

shared = FastAPI()
symmetric = Symmetric()
asymmetric = Asymmetric()


# Symmetric routes
@shared.get("/symmetric/key/", tags=["Symmetric"], summary="Generate the symmetric key")
def getSymmetricKey():
    """
        Return a randomly generated symmetric key in the form of HEX
        :rtype: str
    """
    return userFriendlyResult(symmetric.generateKey())


@shared.post("/symmetric/key/", tags=["Symmetric"], summary="Set the symmetric key on the server")
def postSymmetricKey(key: str) -> bool:
    """
        Set the public and private key on the server in the form of HEX
        (in JSON as dict)
        :rtype: bool
    """
    return userFriendlyResult(symmetric.setKey(key))


@shared.post("/symmetric/encode/", tags=["Symmetric"], summary="Encrypt given message")
def postSymmetricEncrypt(text: str) -> Optional[bytes]:
    """
        Send a message, and return it encrypted
        :rtype: Optional[bytes]
    """
    return userFriendlyResult(symmetric.encrypt(text))


@shared.post("/symmetric/decode/", tags=["Symmetric"], summary="Decrypt given message")
def postSymmetricDecrypt(text: bytes) -> Optional[bytes]:
    """
        Set the symmetric key provided in the form of HEX in request on the server
        :rtype: Optional[bytes]
    """
    return userFriendlyResult(symmetric.decrypt(text))


# Asymmetric routes
@shared.get("/asymmetric/key/", tags=["Asymmetric"], summary="Generate the asymmetric keys, set them on the server "
                                                             "and return them in hex format")
def getAsymmetricKey():
    """
        Return a new public and private key in the form of HEX
        (in JSON as dict) and set it on the server
    """
    privateKey, publicKey = asymmetric.generateKeys()
    asymmetric.setKeys(privateKey, publicKey)
    return userFriendlyResult(asymmetric.getKeysInHex())


@shared.get("/asymmetric/key/ssh", tags=["Asymmetric"], summary="Return asymmetric keys in SSH format")
def getAsymmetricKeySSH():
    """
        Return public and private key in HEX format
        saved in OpenSSH format
    """
    return userFriendlyResult(asymmetric.getKeysInSSH())


@shared.post("/asymmetric/key/", tags=["Asymmetric"], summary="Set asymmetric keys on the server")
def postAsymmetricKey(privateKey, publicKey):
    """
        Set the public and private key on the server in the form of HEX
        (in JSON as dict)
    """
    return userFriendlyResult(asymmetric.setKeys(privateKey, publicKey))


@shared.post("/asymmetric/sign/", tags=["Asymmetric"], summary="Sign a message")
def postSignMessage(message: str):
    """
        Use the currently set private key,
        sign the message and return it with the signed one
    """
    return userFriendlyResult(asymmetric.sign(message))


@shared.post("/asymmetric/verify/", tags=["Asymmetric"], summary="Verify a message")
def postVerifyMessage(message, signature):
    """
        Use the currently set public key,
        verify if the message was encrypted with it
        :rtype: bool
    """

    return asymmetric.verify(message, signature)


@shared.post("/asymmetric/encode/", tags=["Asymmetric"], summary="Encrypt a message")
def postEncrypt(message):
    """
        Send a message, and return it encrypted
    """
    return userFriendlyResult(asymmetric.encrypt(message))


@shared.post("/asymmetric/decode/", tags=["Asymmetric"], summary="Decrypt a message")
def postDecrypt(message):
    """
        Send the message, and return it decrypted
    """
    return userFriendlyResult(asymmetric.decrypt(message))


def userFriendlyResult(result):
    """
        Handle the basic error message if result is None or False
    """
    return "Sorry, something went wrong. Please check if the key is set and " \
           "data is provided the right way" if result is None or False else result
