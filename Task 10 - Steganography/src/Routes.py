from flask import Flask, jsonify, request
from src.Steganography import Steganography
from src.CustomCipher import CustomCipher
from src.CustomDecipher import CustomDecipher

# Instantiate the Node
app = Flask(__name__)

# Instantiate objects
st = Steganography()
cc = CustomCipher()
cd = CustomDecipher()


@app.route('/api/networkstatus', methods=['GET'])
def getNetworkStatus():
    """

        :rtype: str
    """
    return 'The network is working properly'


@app.route('/api/st/encode', methods=['POST'])
def stEncode(src, message, dest):
    response = st.Encode(src, message, dest)
    return jsonify(response), 200


@app.route('/api/st/decode', methods=['POST'])
def stDecode(src):
    response = st.Decode(src)
    return jsonify(response), 200


@app.route('/api/cipher/encode', methods=['POST'])
def cipherEncode():
    text = getTextFromResponse(request.get_json())
    if not text:
        return jsonify('Missing the text value'), 400
    return jsonify(cc.cipher(text)), 200


@app.route('/api/cipher/decode', methods=['POST'])
def cipherDecode():
    text = getTextFromResponse(request.get_json())
    if not text:
        return jsonify('Missing the text value'), 400
    return jsonify(cd.decipher(text)), 200


def getTextFromResponse(response):
    try:
        if not response['text']:
            return None
        return response['text']
    except KeyError:
        return None
