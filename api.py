from eth_utils import is_0x_prefixed
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.models import Model
from pickle import dump
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
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
