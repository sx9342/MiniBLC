import os
import sys
import unittest

# 将 src 目录添加到模块搜索路径
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
sys.path.insert(0, SRC_DIR)

from blockchain import Blockchain


class TestBlockchainTampering(unittest.TestCase):

    def setUp(self):
        """每个测试用例都创建一条全新的区块链"""
        self.blockchain = Blockchain()
        self.blockchain.add_block_to_chain("Hello MiniBLC")
        self.blockchain.add_block_to_chain("Second Block")

    def test_hash_tampering(self):
        """测试一：区块哈希被强行篡改"""
        # 直接修改高度为 1 的区块哈希，不重新计算
        self.blockchain.chain[1].hash = "tampered_hash"

        self.assertFalse(self.blockchain.validate_chain())

    def test_chain_link_tampering(self):
        """测试二：区块前后连接关系被强行篡改"""
        block = self.blockchain.chain[1]

        # 修改前置哈希，破坏区块连接关系
        block.prev_hash = "invalid_prev_hash"

        # 重新计算当前区块哈希，确保自身哈希仍然有效
        block.hash = block.calculate_hash()

        self.assertFalse(self.blockchain.validate_chain())


if __name__ == "__main__":
    unittest.main(verbosity=2)