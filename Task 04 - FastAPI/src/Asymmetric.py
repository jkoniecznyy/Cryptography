from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class Asymmetric:
    """
        Asymmetric
    """
    keys = {
        "privateKey": None,
        "publicKey": None
    }

    def __init__(self):
        pass

    def __updateKeys(self, privateKey):
        """
            Asymmetric
        """
        self.keys["privateKey"] = privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                                           format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                           encryption_algorithm=serialization.NoEncryption()).hex()
        self.keys["publicKey"] = privateKey.public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                                                      format=serialization.PublicFormat.SubjectPublicKeyInfo).hex()

    def createKeys(self):
        """
        Generates a random symmetric key
        :rtype: hex key
        """
        self.__updateKeys(rsa.generate_private_key(public_exponent=65537, key_size=2048))
        return self.keys

    def getSSHKey(self):
        """
            Asymmetric
        """

        return True

    def postKey(self, privateKey, publicKey):
        """
            Asymmetric
        """
        self.keys["privateKey"] = privateKey
        self.keys["publicKey"] = publicKey
        return True

    def sign(self, message):
        """
            Asymmetric
        """
        pass

    def verify(self, message):
        """
            Asymmetric
        """
        pass

    def encode(self, message):
        """
            Asymmetric
        """
        pass

    def decode(self, message):
        """
            Asymmetric
        """
        pass
