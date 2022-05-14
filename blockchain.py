import os
import hashlib,json


class BlockData:
   def __init__(self,owner,imgname,imgfeaturevector):
      self.imgfeaturevector,self.imgname,self.owner = imgfeaturevector,imgname,owner


class BlockChain:
    initialblock=BlockData("bv","acikhack.jpg",[0])
    def __init__(self):
    # Print the linked list
        self.chain=[]
        self.blockrawdata=[]
        self.newBlock(BlockChain.initialblock,"1")
    def newBlock(self,blockdata, preheader_hash=None):
        prehash=preheader_hash or self.hash(self.chain[-1])
        newblockheader = {'preheader_hash':prehash,'datahash':self.hash(blockdata)}
        self.chain.append(newblockheader)
        self.blockrawdata.append(blockdata)
    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    @property
    def last_block(self):
        return self.chain[-1]


