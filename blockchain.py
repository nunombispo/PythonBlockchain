import time
from block import Block
from timeit import default_timer as timer
from datetime import timedelta


class Blockchain:
    def __init__(self):
        self.new_data = []
        self.chain = []
        self.difficulty = 1
        self.__create_genesis_block()

    def __create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def __proof_of_work(self, block):
        start = timer()
        block.nonce = 0
        computed_hash = block.compute_hash()
        print('Mining block {}'.format(block.index))
        print('Difficulty: {}'.format(self.difficulty))
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        print('Computed hash: {}'.format(computed_hash))
        print('Nonce: {}'.format(block.nonce))
        end = timer()
        print('Elapsed time: {}'.format(timedelta(seconds=end - start)))
        return computed_hash

    def __is_valid_proof(self, block, block_hash):
        return block_hash.startswith('0' * self.difficulty) and block_hash == block.compute_hash()

    def __add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.__is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def add_new_data(self, data):
        self.new_data.append(data)

    def mine(self):
        if not self.new_data:
            return False
        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
                          data=self.new_data,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.__proof_of_work(new_block)
        self.__add_block(new_block, proof)
        self.new_data = []
        return new_block.index

    @property
    def last_block(self):
        return self.chain[-1]