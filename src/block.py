import hashlib
import time
class Block:
    def __init__(self,data:str,prev_hash:str = "0",height:int = 0):
        self.data = data
        self.timestamp = int(time.time())
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()
        self.height = height

    def calculate_hash(self):
        sha256_hash = hashlib.sha256()
        digests = self.data + "|" + str(self.timestamp) + "|" + self.prev_hash
        sha256_hash.update(digests.encode())
        return str(sha256_hash.hexdigest())


