from fastapi import FastAPI
from src.Asymmetric import Asymmetric
from src.Symmetric import Symmetric

shared = FastAPI()

symmetric = Symmetric()
asymmetric = Asymmetric()


# Symmetric routes
@shared.get("/symmetric/key/")
def getSymmetricKey():
    return symmetric.createKey()


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
    return asymmetric.createKeys()


# todo SSH
@shared.get("/asymmetric/key/ssh")
def getAsymmetricKey():
    return asymmetric.createKeys()


@shared.post("/asymmetric/key/")
def postAsymmetricKey(privateKey, publicKey):
    return asymmetric.postKey(privateKey, publicKey)


@shared.post("/asymmetric/sign/")
def postSignMessage(message):
    return asymmetric.sign(message)


@shared.post("/asymmetric/verify/")
def postVerifyMessage(message):
    return asymmetric.verify(message)


@shared.post("/asymmetric/encode/")
def postEncode(message):
    return asymmetric.encode(message)


@shared.post("/asymmetric/decode/")
def postDecode(message):
    return asymmetric.decode(message)
