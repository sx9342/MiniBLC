from block import Block
class Blockchain:
    def __init__(self): # 初始化区块链，保证第一个区块一定是创世区块
        self.chain = []
        self.chain.append(self.genesis_block())

    def genesis_block(self) -> Block: # 初始化创世区块
        genesis_block = Block("GenesisBlock","0",0)
        return genesis_block

    def add_block_to_chain(self,data:str):
        previous_block = self.chain[-1]
        new_block = Block(
            data,
            previous_block.hash,
            previous_block.height + 1
        )
        self.chain.append(new_block)

