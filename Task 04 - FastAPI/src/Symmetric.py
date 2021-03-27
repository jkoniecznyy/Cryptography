from cryptography.fernet import Fernet


class Symmetric:
    """
        Symmetric
    """
    key = ''

    def __init__(self):
        pass

    def createKey(self) -> hex:
        """
        Genrates a random symmetric key
        :rtype: hex key
        """
        return Fernet.generate_key().hex()

    def setKey(self, key: hex) -> True:
        """

        """
        self.key = key
        return True

    def encode(self, text: str):
        """

        """
        f = Fernet(bytearray.fromhex(self.key))
        return f.encrypt(text.encode())

    def decode(self, text: bytes) -> bytes:
        """

        """
        f = Fernet(bytearray.fromhex(self.key))
        return f.decrypt(text)
