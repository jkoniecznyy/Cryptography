from fastapi import FastAPI
from src.Blockchain import Blockchain
from typing import Optional

shared = FastAPI()
blockchain = Blockchain()


@shared.get("/networkstatus/", tags=["blockchain"], summary="")
def getNetworkStatus() -> bool:
    """
        Return a randomly generated symmetric key in the form of HEX
        :rtype: hex
    """
    return True


@shared.get("/balance/", tags=["blockchain"], summary="")
def getBalance() -> str:
    """
        Return a randomly generated symmetric key in the form of HEX
        :rtype: hex
    """
    return 'True'


@shared.post("/newtransaction/", tags=["blockchain"], summary="")
def postNewTransaction() -> str:
    """
        Return a randomly generated symmetric key in the form of HEX
        :rtype: hex
    """
    return 'True'


def userFriendlyResult(result):
    """
        Handle the basic error message if result is None or False
    """
    return "Sorry, something went wrong. Please check if the key is set and " \
           "data is provided the right way" if result is None or False else result
