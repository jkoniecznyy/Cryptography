import unittest
from src.Blockchain import Blockchain


class BlockchainTest(unittest.TestCase):

    def test_last_block(self):
        blockchain = Blockchain()
        last_block = blockchain.last_block
        self.assertEqual(last_block['index'], 1)

