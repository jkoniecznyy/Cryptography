from cryptography.fernet import Fernet
from typing import Optional
import logging


class Symmetric:
    """
        Allows to:
        - generate and set the symmetric key
        - encode and decode a text, by using previously set key
    """
    key = None

    def __init__(self):
        logging.info('Symmetric - class created')
        pass

    def generateKey(self) -> Optional[hex]:
        """
            Generate a random symmetric key
            :rtype: Optional[hex]
        """
        logging.info('Symmetric - Generating a key')
        try:
            return Fernet.generate_key().hex()
        except Exception as ex:
            logging.error(ex)
            return None

    def setKey(self, key: hex) -> bool:
        """
            Save a key on the server
            :rtype: bool
        """
        logging.info('Symmetric - Setting the key')
        self.key = key
        return True

    def encrypt(self, text: str) -> Optional[bytes]:
        """
            Encode a text
            :rtype: Optional[bytes]
        """
        logging.info('Symmetric - Encoding the text')
        if self.key is not None:
            try:
                f = Fernet(bytearray.fromhex(self.key))
                return f.encrypt(text.encode())
            except Exception as ex:
                logging.error(ex)
                return None
        else:
            return None

    def decrypt(self, text: bytes) -> Optional[str]:
        """
            Decode a text
            :rtype: Optional[bytes]
        """
        logging.info('Symmetric - Decoding the text')
        if self.key is not None:
            try:
                f = Fernet(bytearray.fromhex(self.key))
                return f.decrypt(text).decode()
            except Exception as ex:
                logging.error(ex)
                return None
        else:
            return None
