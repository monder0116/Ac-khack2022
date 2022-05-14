import os
import hashlib,json


class BlockData:
    def __init__(self,owner,imgname,imgfeaturevector):
        self.imgfeaturevector,self.imgname,self.owner = imgfeaturevector,imgname,owner

    def hash(self):
        block_string = json.dumps((self.owner,self.imgname,self.imgfeaturevector), sort_keys=True).encode()
        return block_string
    def isEqual(self,newdata):
        return newdata.imgname==self.imgname
    
class BlockChain:
    initialblock=BlockData("bv","acikhack.jpg",[])
    def __init__(self):
        self.chain=[]
        self.newBlock(BlockChain.initialblock,"1")
    def newBlock(self,newblockdata, preheader_hash=None):
        self.checkisdesignvalid(newblockdata)
        prehash=preheader_hash or self.hash(self.chain[-1])
        print("prehash:",prehash)
        newblockheader = {'preheader_hash':prehash,'blockdata':newblockdata }
        self.chain.append(newblockheader)
    def checkisdesignvalid(self,newblockdata):
        for data in self.chain:
            blockdata=data['blockdata']
            if blockdata.isEqual(newblockdata):
                print("eklenemezzzzzzzz","-",blockdata.imgfeaturevector)
                break
    @staticmethod
    def hash(block):
        block_string = json.dumps((block['preheader_hash'],block['blockdata'].imgname), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    @property
    def last_block(self):
        return self.chain[-1]
