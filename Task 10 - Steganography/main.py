if __name__ == '__main__':
    from argparse import ArgumentParser
    from src.Routes import app

    # from src.Steganography import Steganography
    # from src.CustomCipher import CustomCipher
    # from src.CustomDecipher import CustomDecipher

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)

    # main function
    # print("--Welcome to $t3g0--")
    # print("1: Encode")
    # print("2: Decode")
    # St = Steganography()
    # func = input()
    #
    # if func == '1':
    #     print("Enter Source Image Path")
    #     src = input()
    #     print("Enter Message to Hide")
    #     message = input()
    #     print("Enter Destination Image Path")
    #     dest = input()
    #     print("Encoding...")
    #     St.Encode(src, message, dest)
    #
    # elif func == '2':
    #     print("Enter Source Image Path")
    #     src = input()
    #     print("Decoding...")
    #     St.Decode(src)
    #
    # else:
    #     print("ERROR: Invalid option chosen")
