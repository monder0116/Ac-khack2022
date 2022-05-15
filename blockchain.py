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
    initialblock =None
    similarity_th_ratio=0.5
    def __init__(self):
        self.chain = []
        self.newBlock(BlockData("","",[1]), "1")
    def newBlock(self, newblockdata, preheader_hash=None):
        checkres,similarblock=self.checkChainIsvalid(newblockdata)
        if not checkres:
            return None,similarblock
        prehash = preheader_hash or self.hash(self.chain[-1])
        newblockheader = {'preheader_hash': prehash, 'blockdata': newblockdata}
        if len(self.chain)==0:
            BlockChain.initialblock=newblockheader
        self.chain.append(newblockheader)
        return newblockheader,None
    def checkChainIsvalid(self, newblockdata):
        '''
        return "chain valid status as bool variable":bool and "if has similar, similar block instance":BlockDict 
        '''
        liste = [item['blockdata'].imgname for item in self.chain if item != BlockChain.initialblock]
        comparator = ImageComparator(liste)
        for data in self.chain:
            simratio=comparator.calculateResultsFor(newblockdata.imgname)
            if  simratio> BlockChain.similarity_th_ratio:
                return False,data
        return True,None
    @staticmethod
    def hash(block):
        block_string = json.dumps(
            (block['preheader_hash'], block['blockdata'].imgname), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
