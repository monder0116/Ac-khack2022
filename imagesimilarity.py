

import cv2 ,os
import pickle,glob
import matplotlib.pyplot as plt

class ImageFeatureExtractor:
    detector = cv2.xfeatures2d.SIFT_create()
    def __init__(self,imgpath):
        self.imgpath=imgpath
        self.image=ImageFeatureExtractor.imageResizeTrain(cv2.imread(self.imgpath,0))
    @staticmethod
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
    def extract(self):
        keypoint,descriptor= ImageFeatureExtractor.detector.detectAndCompute(self.image, None)
        #deserialize Keypoints
        deserializedKeypoints = []
        filepath = "kp/" + str(self.imgpath.split('/')[-1].split('.')[0].strip()) + ".txt"
        for point in keypoint:
            temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id)
            deserializedKeypoints.append(temp)
        with open(filepath, 'wb') as fp:
            pickle.dump(deserializedKeypoints, fp)    

        #deserialize descriptor
        filename = "{}.txt".format(str(self.imgpath.split('/')[-1].split('.')[0].strip()))
        filepath=os.path.join("templates","featuredb",filename)
        with open(filepath, 'wb') as fp:
            pickle.dump(descriptor, fp)
        return (keypoint,descriptor)

class ImageComparator:
    bf = cv2.BFMatcher()
    def __init__(self,allblockimgnamelist:list):
        self.allblockimgnamelist=allblockimgnamelist
    @staticmethod
    def fetchKeypointFromFile(i):
        filepath = "kp/{}.txt".format( i.strip())
        print(filepath)
        print("kp file exist=",os.path.exists(filepath))
        keypoint = []

        file = open(filepath,'rb')
        deserializedKeypoints = pickle.load(file)
        file.close()
        for point in deserializedKeypoints:
            temp = cv2.KeyPoint(point[0][0],point[0][1],point[1], point[2], point[3], point[4], point[5])
            keypoint.append(temp)
        return keypoint

    @staticmethod
    def fetchDescriptorFromFile(i):
        filename = "{}.txt".format( i.strip())
        filepath=os.path.join("templates","featuredb",filename)

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

    def calculateResultsFor(self,newimagename):
        if len(self.allblockimgnamelist)==0:
            return 0
        keypoint1 = ImageComparator.fetchKeypointFromFile(newimagename)
        descriptor1 = ImageComparator.fetchDescriptorFromFile(newimagename)
        maxscore=0
        for j in self.allblockimgnamelist:
            keypoint2 = ImageComparator.fetchKeypointFromFile(j)
            descriptor2 =ImageComparator.fetchDescriptorFromFile(j)
            matches = ImageComparator.calculateMatches(descriptor1, descriptor2)
            score = ImageComparator.calculateScore(len(matches),len(keypoint1),len(keypoint2))  
            if score>maxscore:
                maxscore=score
        return maxscore
