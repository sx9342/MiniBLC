from block import Block
from blockchain import Blockchain



class Query:
    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain
    def get_chain_nums(self):
        return len(self.blockchain.chain)

    def get_chain_height(self):
        return self.blockchain.get_latest_block().height
    # 根据区块高度查询区块信息
    def query_block_by_height(self, height: int) -> Block | None:
        if height < 0 or height >= len(self.blockchain.chain):
            return None

        return self.blockchain.chain[height]