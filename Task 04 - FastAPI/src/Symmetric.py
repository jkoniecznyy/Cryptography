from cryptography.fernet import Fernet


class Symmetric:
    """
        Symmetric
    """
    key = None

    def __init__(self):
        pass

    def generateKey(self) -> hex:
        """
        Generates a random symmetric key
        :rtype: hex key
        """
        return Fernet.generate_key().hex()

    def setKey(self, key: hex) -> True:
        """

        """
        self.key = key
        return True

    def encode(self, text: str) -> bytes:
        """

        """
        f = Fernet(bytearray.fromhex(self.key))
        return f.encrypt(text.encode())

    def decode(self, text: bytes) -> bytes:
        """

        """
        f = Fernet(bytearray.fromhex(self.key))
        return f.decrypt(text)
