from fastapi import FastAPI
from src.Symmetric import Symmetric

shared = FastAPI()

sym = Symmetric()


@shared.get("/symmetric/key/")
def getSymmetricKey():
    return sym.createKey()


@shared.post("/symmetric/key/")
def postSymmetricKey(key: str):
    sym.setKey(key)
    return 'Mission succeeded'


@shared.post("/symmetric/encode/")
def postSymmetricEncode(text: str):
    return sym.encode(text)


@shared.post("/symmetric/decode/")
def postSymmetricDecode(text: bytes):
    return sym.decode(text)
