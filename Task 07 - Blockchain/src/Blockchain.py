import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Never gonna give you up", proof=100)

    def new_block(self, proof, previous_hash=None):
        """
            Create a new block listing key/value pairs of block information in a JSON object.
            Reset the list of pending transactions & append the newest block to the chain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):
        """
            Search the blockchain for the most recent block.
        """
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        """
            Add a transaction with relevant info to the 'blockpool' - list of pending tx's.
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        """
            Receive one block. Turn it into a string, turn that into Unicode (for hashing).
            Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.
        """
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
