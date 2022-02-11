import hashlib
import json


class Block:
    def __init__(self, index, data, timestamp, previous_hash, nonce=0):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return 'Block: {}'.format(self.__dict__)