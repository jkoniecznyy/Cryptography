from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import logging
import base64


class Asymmetric:
    """
        Allows to:
        - Generate, set and get public key and private key,
        - Sign and verify a text,
        - Encode and decode a text
    """
    privateKey = None
    publicKey = None

    def __init__(self):
        logging.info('Asymmetric - class created')
        pass

    def setKeys(self, privateKey, publicKey):
        """
            setKeys
        """
        logging.info('Asymmetric - Setting keys')
        self.privateKey = privateKey
        self.publicKey = publicKey
        return True

    def getKeys(self):
        """
            getKeys
        """
        logging.info('Asymmetric - Getting keys')
        return self.privateKey, self.publicKey

    def getKeysInHex(self):
        """
            getKeysInHex
        """
        logging.info('Asymmetric - Getting keys as Hex')
        privateKeyHex = self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()

        publicKeyHex = self.publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).hex()

        return {
            "privateKeyHex": privateKeyHex,
            "publicKeyHex": publicKeyHex
        }

    def getKeysInSSH(self):
        """
            getKeysInSSH
        """
        logging.info('Asymmetric - Getting keys as SSH')
        privateKeySSH = self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption()
        ).hex()

        publicKeySSH = self.publicKey.public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        ).hex()

        return {
            "privateKeySSH": privateKeySSH,
            "publicKeySSH": publicKeySSH
        }

    def generateKeys(self):
        """
            Generate a random asymmetric key
            :rtype:
        """
        logging.info('Asymmetric - Generating the keys')
        privateKey = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend())
        publicKey = privateKey.public_key()

        return [privateKey, publicKey]

    def sign(self, message: str):
        """
            sign
        """
        logging.info('Asymmetric - Signing the message')
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
            verify
        """
        logging.info('Asymmetric - Verifying the message')
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
            encrypt
        """
        logging.info('Asymmetric - Encoding the text')
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
            decode
        """
        logging.info('Asymmetric - Decoding the text')
        plaintext = self.privateKey.decrypt(
            base64.b64decode(message),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext
