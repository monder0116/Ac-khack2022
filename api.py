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
mainchain=BlockChain()


def append2Chain(owner,imgpath):
    block=createAndReturnBlock(owner,imgpath)
    mainchain.newBlock(block)
    for i in mainchain.chain:
        print("block:",i)
    return block
def createAndReturnBlock(owner,imgpath):
    vector=getimgFeatureVector(imgpath)
    return BlockData(owner,imgpath.split(os.path.sep)[-1],vector)

def getimgFeatureVector(imgpath):
    model = VGG16(weights='imagenet', include_top=True)
    img = image.load_img(imgpath, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    vgg16_feature = model.predict(img_data)
    return vgg16_feature[0]