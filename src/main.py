from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_block_to_chain("Hello MiniBLC")
blockchain.add_block_to_chain("Second Block")

for b in blockchain.chain:
    print(f"Height: {b.height}")
    print(f"Data: {b.data}")
    print(f"Timestamp: {b.timestamp}")
    print(f"PrevHash: {b.prev_hash}")
    print(f"Hash: {b.hash}")
    print("-" * 60)