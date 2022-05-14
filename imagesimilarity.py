

import cv2 
import pickle,glob
import matplotlib.pyplot as plt

class ImageFeatureExtractor:
    detector = cv2.xfeatures2d.SIFT_create()
    def __init__(self,imgname):
        pass
    def imageResizeTrain(image):
        maxD = 1024
        height,width = image.shape
        aspectRatio = width/height
        if aspectRatio < 1:
            newSize = (int(maxD*aspectRatio),maxD)
        else:
            newSize = (maxD,int(maxD/aspectRatio))
        image = cv2.resize(image,newSize)
        return image
    def extract():
        return ImageFeatureExtractor.detector.detectAndCompute(image, None)
    def createKPfile(self):
class ImageComparator:
    bf = cv2.BFMatcher()
    def __init__(self,sourceimgname:str,allblockimgnamelist:list):
        self.sourceimgname=sourceimgname
        self.allblockimgnamelist=allblockimgnamelist
        self.calculateResultsFor()
    @staticmethod
    def fetchKeypointFromFile(i):
        filepath = "kp/" + i + ".txt"
        keypoint = []
        file = open(filepath,'rb')
        deserializedKeypoints = pickle.load(file)
        file.close()
        for point in deserializedKeypoints:
            temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
            keypoint.append(temp)
        return keypoint

    @staticmethod
    def fetchDescriptorFromFile(self,i):
        filepath = "ds/"+ i + ".txt"
        file = open(filepath,'rb')
        descriptor = pickle.load(file)
        file.close()
        return descriptor



    @staticmethod
    def calculateScore(matches,keypoint1,keypoint2):
        return 100 * (matches/min(keypoint1,keypoint2))
    @staticmethod
    def calculateMatches(des1,des2):
        matches = ImageComparator.bf.knnMatch(des1,des2,k=2)
        topResults1 = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                topResults1.append([m])
                
        matches = ImageComparator.bf.knnMatch(des2,des1,k=2)
        topResults2 = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                topResults2.append([m])
        
        topResults = []
        for match1 in topResults1:
            match1QueryIndex = match1[0].queryIdx
            match1TrainIndex = match1[0].trainIdx

            for match2 in topResults2:
                match2QueryIndex = match2[0].queryIdx
                match2TrainIndex = match2[0].trainIdx

                if (match1QueryIndex == match2TrainIndex) and (match1TrainIndex == match2QueryIndex):
                    topResults.append(match1)
        return topResults

    
    def calculateResultsFor(self):
        keypoint1 = ImageComparator.fetchKeypointFromFile(self.sourceimgname)
        descriptor1 = ImageComparator.fetchDescriptorFromFile(self.sourceimgname)
        maxscore=-1
        for j in self.allblockimgnamelist:
            keypoint2 = ImageComparator.fetchKeypointFromFile(j)
            descriptor2 =ImageComparator.fetchDescriptorFromFile(j)
            matches = ImageComparator.calculateMatches(descriptor1, descriptor2)
            score = ImageComparator.calculateScore(len(matches),len(keypoint1),len(keypoint2))  
            if score>maxscore:
                maxscore=score
        return maxscore
