import numpy as np
from pip import main
# load an image from file
from blockchain import BlockChain,BlockData
import os
from imagesimilarity import ImageFeatureExtractor,ImageComparator
mainchain=BlockChain()


def append2Chain(owner,imgpath):
    block=createAndReturnBlock(owner,imgpath)
    result=mainchain.newBlock(block)
    if not result:
        return None
    for i in mainchain.chain:
        print("block:",i)
    return block
def createAndReturnBlock(owner,imgpath):
    extrator=ImageFeatureExtractor(imgpath)
    vector= extrator.extract()
    return BlockData(owner,imgpath.split(os.path.sep)[-1].split('.')[0],vector)
