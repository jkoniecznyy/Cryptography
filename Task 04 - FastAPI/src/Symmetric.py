from typing import Optional

from cryptography.fernet import Fernet
import logging


class Symmetric:
    """
        Allows to generate and set symmetric key
        and to encode and decode a text,
        by using previously set key
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
        try:
            self.key = key
            return True
        except Exception as ex:
            logging.error(ex)
            return False

    def encode(self, text: str) -> Optional[bytes]:
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

    def decode(self, text: bytes) -> Optional[bytes]:
        """
            Decode a text
            :rtype: Optional[bytes]
        """
        logging.info('Symmetric - Decoding the text')
        if self.key is not None:
            try:
                f = Fernet(bytearray.fromhex(self.key))
                return f.decrypt(text)
            except Exception as ex:
                logging.error(ex)
                return None
        else:
            return None
