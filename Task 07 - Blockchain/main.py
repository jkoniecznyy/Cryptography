from src.Blockchain import Blockchain
from src.Routes import shared
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    shared
    blockchain = Blockchain()
    t1 = blockchain.new_transaction("Jurek", "Rick Astley", '5 BTC')
    t2 = blockchain.new_transaction("Tomek", "Rick Astley", '1 BTC')
    t3 = blockchain.new_transaction("xxxFanNr1xxx", "Rick Astley", '5 BTC')
    blockchain.new_block(12345)

    t4 = blockchain.new_transaction("Mike", "Rick Astley", '1 BTC')
    t5 = blockchain.new_transaction("Alice", "Rick Astley", '0.5 BTC')
    t6 = blockchain.new_transaction("Bob", "Rick Astley", '0.5 BTC')
    blockchain.new_block(6789)

    print("Genesis block: ", blockchain.chain)
    print("Genesis block: ", t1)
    print("Genesis block: ", t2)
    print("Genesis block: ", t3)