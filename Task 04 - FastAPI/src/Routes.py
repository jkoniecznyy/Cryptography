from fastapi import FastAPI
from src.Asymmetric import Asymmetric
from src.Symmetric import Symmetric

shared = FastAPI()

symmetric = Symmetric()
asymmetric = Asymmetric()


# Symmetric routes
@shared.get("/symmetric/key/")
def getSymmetricKey():
    return symmetric.generateKey()


@shared.post("/symmetric/key/")
def postSymmetricKey(key: str):
    symmetric.setKey(key)
    return 'Mission succeeded'


@shared.post("/symmetric/encode/")
def postSymmetricEncode(text: str):
    return symmetric.encode(text)


@shared.post("/symmetric/decode/")
def postSymmetricDecode(text: bytes):
    return symmetric.decode(text)


# Asymmetric routes
@shared.get("/asymmetric/key/")
def getAsymmetricKey():
    privateKey, publicKey = asymmetric.generateKeys()
    asymmetric.setKeys(privateKey, publicKey)
    return asymmetric.getKeysInHex()


# todo SSH
@shared.get("/asymmetric/key/ssh")
def getAsymmetricKeySSH():
    return asymmetric.generateKey()


@shared.post("/asymmetric/key/")
def postAsymmetricKey(privateKey, publicKey):
    return asymmetric.setKeys(privateKey, publicKey)


@shared.post("/asymmetric/sign/")
def postSignMessage(message: str):
    return asymmetric.sign(message)


@shared.post("/asymmetric/verify/")
def postVerifyMessage(message, signature):
    return asymmetric.verify(message, signature)


@shared.post("/asymmetric/encode/")
def postEncode(message):
    return asymmetric.encrypt(message)


@shared.post("/asymmetric/decode/")
def postDecode(message):
    return asymmetric.decode(message)
