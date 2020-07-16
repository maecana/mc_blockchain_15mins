# python imports
import hashlib


# Block
class Block:
    # define initialization
    # @params : prev_hash - hash of the previous block
    #           transactions - transaction being created now
    # return void
    def __init__(self, prev_hash, transactions):
        self.prev_hash = prev_hash
        self.transactions = "".join(transactions)
        self.block_hash = hashlib.sha256(self.transactions.encode()).hexdigest()