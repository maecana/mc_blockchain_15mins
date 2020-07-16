# app imports
from Block import Block

# Global variables
blockchain = []

genesis_block = Block("The Time 03/09/2009 Chancellor on the brink of second bailouts for banks", ["Satoshi Nakamoto sent 5 BTC to Hal finney",
                      "A sent 5 BTC to B"])

print("HASH BLOCK: Genesis Block", genesis_block.block_hash)
second_block = Block(genesis_block.block_hash, ["B sent 4 BTC to C", "C sent 3 BTC to D"])
print("HASH BLOCK: Second Block", second_block.block_hash)