from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import logging
import base64


class Asymmetric:
    """
        Asymmetric
    """
    privateKey = None
    publicKey = None

    def __init__(self):
        pass

    def setKeys(self, privateKey, publicKey):
        """
            Asymmetric
        """
        self.privateKey = privateKey
        self.publicKey = publicKey
        return True

    def getKeys(self):
        """
            Asymmetric
        """
        return self.privateKey, self.publicKey

    def getKeysInHex(self):
        """
            Asymmetric
        """
        privateKeyHex = self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()

        publicKeyHex = self.publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex()

        keysHex = {
            "privateKeyHex": privateKeyHex,
            "publicKeyHex": publicKeyHex
        }

        return keysHex

    def generateKeys(self):
        """
        Generates a random asymmetric key
        :rtype: hex key
        """
        logging.warning('generateKeys')
        privateKey = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend())
        publicKey = privateKey.public_key()

        return [privateKey, publicKey]

    def getSSHKey(self):
        """
            Asymmetric
        """

        return True

    def sign(self, message: str):
        """
            Asymmetric
        """
        logging.warning('sign')
        signature = self.privateKey.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature)

    def verify(self, message, signature):
        """
            Asymmetric
        """
        logging.warning('verify')
        return self.publicKey.verify(
            base64.b64decode(signature),
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def encrypt(self, message: str) -> bytes:
        """
            Asymmetric
        """
        ciphertext = self.publicKey.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(ciphertext)

    def decode(self, message: bytes):
        """
            Asymmetric
        """
        plaintext = self.privateKey.decrypt(
            base64.b64decode(message),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext
