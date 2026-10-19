from block import Block
class Blockchain:
    def __init__(self): # 初始化区块链，保证第一个区块一定是创世区块
        self.chain = []
        self.chain.append(self.genesis_block())

    def genesis_block(self) -> Block: # 初始化创世区块
        genesis_block = Block("GenesisBlock","0",0)
        return genesis_block
    def get_latest_block(self):
        return self.chain[-1]

    def add_block_to_chain(self,data:str):
        previous_block = self.chain[-1]
        new_block = Block(
            data,
            previous_block.hash,
            previous_block.height + 1
        )
        self.chain.append(new_block)
    # 验证区块链是否合法
    def validate_chain(self) -> bool:
        # 验证创世区块
        if len(self.chain) == 1:
            if self.chain[0].hash == self.chain[0].calculate_hash():
                if self.chain[0].prev_hash != "0":
                    print("创世区块前置哈希错误")
                    return False
                if self.chain[0].height != 0:
                    print("创世区块高度错误")
                    return False
                if self.chain[0].hash != self.chain[0].calculate_hash():
                    print("创世区块被篡改")
                    return False
                return True
        # 验证其他区块
        for i in range(1,len(self.chain)):
            block_to_validate = self.chain[i]
            # 验证当前数据是否篡改
            if block_to_validate.hash != block_to_validate.calculate_hash():
                print(f"高度为 {i} 的区块数据篡改")
                return False

            # 验证prev_hash是否等于前一区块的hash
            prev_block = self.chain[i-1]
            if block_to_validate.prev_hash != prev_block.hash:
                print(f"高度为 {i} 的区块前后断裂")
                return False
        return True
