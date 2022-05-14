import os
import hashlib
import json
from imagesimilarity import ImageComparator


class BlockData:
    def __init__(self, owner, imgname, imgfeaturevector):
        self.imgfeaturevector, self.imgname, self.owner = imgfeaturevector, imgname, owner
        
    def hash(self):
        block_string = json.dumps(
            (self.owner, self.imgname, self.imgfeaturevector), sort_keys=True).encode()
        return block_string


class BlockChain:
    initialblock = BlockData("bv", "acikhack.jpg", [])

    def __init__(self):
        self.chain = []
        self.newBlock(BlockChain.initialblock, "1")

    def newBlock(self, newblockdata, preheader_hash=None):
        if not self.checkisdesignvalid(newblockdata):
            return False
        prehash = preheader_hash or self.hash(self.chain[-1])
        newblockheader = {'preheader_hash': prehash, 'blockdata': newblockdata}
        self.chain.append(newblockheader)
        return True
    def checkisdesignvalid(self, newblockdata):
        liste = [item['blockdata'].imgname for item in self.chain if item['blockdata'].imgname !=
                 BlockChain.initialblock.imgname]
        comparator = ImageComparator(liste)
        for data in self.chain:
            blockdata = data['blockdata']
            simratio=comparator.calculateResultsFor(newblockdata.imgname)
            if  simratio> 0.5:
                print("simratio=",simratio)
                print("eklenemezzzzzzz", "-", newblockdata.imgfeaturevector)
                return False
        return True

    @staticmethod
    def hash(block):
        block_string = json.dumps(
            (block['preheader_hash'], block['blockdata'].imgname), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
