from flask import Flask, jsonify, request
from src.Steganography import Steganography
from src.CustomCipher import CustomCipher
from src.CustomDecipher import CustomDecipher

# Instantiate the Node
app = Flask(__name__)

# Instantiate objects
cc = CustomCipher()
cd = CustomDecipher()
st = Steganography()


@app.route('/api/st/encode', methods=['POST'])
def stEncode():
    """
        Check if all the data is provided correctly and call the Steganography.Encode function
        Example:
            {
                "src": "img1.png",
                "message": "Studenci powinni czesciej chodzic na piwo",
                "dest": "hidden.png"
            }
        :rtype: str
    """
    values = request.get_json()
    required = ['src', 'message', 'dest']
    if not all(k in values for k in required):
        return 'Missing values', 400

    response = st.Encode(values['src'], values['message'], values['dest'])
    return jsonify(response), 200


@app.route('/api/st/decode', methods=['POST'])
def stDecode():
    """
        Check if the response contains the "src" field and call the Steganography.Decode function
        Example:
            {
                "src": "hidden.png"
            }
        :rtype: str
    """
    data = request.get_json()
    try:
        if not data['src']:
            return jsonify('Missing the src value'), 400
        return jsonify(st.Decode(data['src'])), 200
    except KeyError:
        return jsonify('Missing the src value'), 400


@app.route('/api/cipher/encode', methods=['POST'])
def cipherEncode():
    """
        Check if all the data is provided correctly and call the CustomCipher.cipher function
        Example:
            {
                "text": "Studenci powinni czesciej chodzic na piwo"
            }
        :rtype: str
    """
    text = getTextFromResponse(request.get_json())
    print(text)
    if not text:
        return jsonify('Missing the text value'), 400
    return jsonify(cc.cipher(text)), 200


@app.route('/api/cipher/decode', methods=['POST'])
def cipherDecode():
    """
        Check if all the data is provided correctly and call the CustomDecipher.decipher function
        Example:
            {
                "text": "bcnvrprmawvjkpfehbnbcfmavpavaprqqvjvbrpgua"
            }
        :rtype: str
    """
    text = getTextFromResponse(request.get_json())
    if not text:
        return jsonify('Missing the text value'), 400
    return jsonify(cd.decipher(text)), 200


def getTextFromResponse(response):
    """
        Check if the response contains the "text" field
    """
    try:
        if not response['text']:
            return None
        return response['text']
    except KeyError:
        return None
