from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from typing import Optional
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

    def setKeys(self, privateKey: RSAPrivateKey, publicKey: RSAPublicKey) -> bool:
        """
            Save public and private key on the server
            :rtype: bool
        """
        logging.info('Asymmetric - Setting keys')
        self.privateKey = privateKey
        self.publicKey = publicKey
        return True

    # TODO fix this function
    def setKeysFromHex(self, privateKey: hex, publicKey: hex) -> bool:
        """
            Save public and private key on the server
            :rtype: bool
        """
        logging.info('Asymmetric - Setting keys from hex')
        try:
            public_key: bytes = bytes.fromhex(publicKey)
            private_key: bytes = bytes.fromhex(privateKey)
        except Exception as ex:
            logging.error(ex)
            return False
        print(private_key)
        print(public_key)
        self.privateKey = private_key
        self.publicKey = public_key
        return True

    def getKeysInHex(self) -> Optional[dict[hex, hex]]:
        """
            Get public and private key in the HEX format
            :rtype: Optional[dict[hex, hex]]
        """
        logging.info('Asymmetric - Getting keys as Hex')
        try:
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
        except Exception as ex:
            logging.error(ex)
            return None

    def getKeysInSSH(self) -> Optional[dict[hex, hex]]:
        """
            Get public and private key in the SSH HEX format
            :rtype: Optional[dict[hex, hex]]
        """
        logging.info('Asymmetric - Getting keys as SSH')
        try:
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
        except Exception as ex:
            logging.error(ex)
            return None

    def generateKeys(self) -> Optional[tuple[RSAPrivateKey, RSAPublicKey]]:
        """
            Generate random asymmetric keys
            :rtype: Optional[tuple[RSAPrivateKey, RSAPublicKey]]
        """
        logging.info('Asymmetric - Generating the keys')
        try:
            privateKey = rsa.generate_private_key(
                public_exponent=65537, key_size=2048, backend=default_backend())
            publicKey = privateKey.public_key()

            return privateKey, publicKey
        except Exception as ex:
            logging.error(ex)
            return None

    def sign(self, text: str) -> Optional[bytes]:
        """
            Sing a text
            :rtype: Optional[bytes]
        """
        logging.info('Asymmetric - Signing the message')
        try:
            signature = self.privateKey.sign(
                text.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return base64.b64encode(signature)
        except Exception as ex:
            logging.error(ex)
            return None

    def verify(self, text: str, signature: bytes) -> bool:
        """
            Verify a text
            :rtype: bool
        """
        logging.info('Asymmetric - Verifying the message')
        try:
            self.publicKey.verify(
                base64.b64decode(signature),
                text.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as ex:
            logging.error(ex)
            return False

    def encrypt(self, text: str) -> Optional[bytes]:
        """
            Encrypt a text (str)
            :rtype: Optional[bytes]
        """
        logging.info('Asymmetric - Encoding the text')
        try:
            ciphertext = self.publicKey.encrypt(
                text.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return base64.b64encode(ciphertext)
        except Exception as ex:
            logging.error(ex)
            return None

    def decrypt(self, text: bytes) -> Optional[bytes]:
        """
            Decrypt a text (bytes)
            :rtype: Optional[bytes]
        """
        logging.info('Asymmetric - Decoding the text')
        try:
            plaintext = self.privateKey.decrypt(
                base64.b64decode(text),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return plaintext.decode()
        except Exception as ex:
            logging.error(ex)
            return None
