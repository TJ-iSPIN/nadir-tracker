import math
import numpy as np
import cv2
from PIL import Image, ImageOps
import os

class blurImg:
    def __init__(self, filename):
        self.filename = filename
    
    def blur(self):
        
        inputSize = (720, 720)
        imgName = self.filename
        img = cv2.imread(imgName)  # Read image
        t_lower = 50
        t_upper = 200
        aperture_size = 5  # Aperture size
        image = Image.open(imgName)

        img[img > 20] = 255

        edge = cv2.Canny(img, t_lower, t_upper, 
                        apertureSize=aperture_size)

        gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #cv2.imshow('original', img)
        #cv2.imshow('edge', edge)

        blur = cv2.GaussianBlur(gs,(5,5),0)
        blur[blur > 50] = 255

        #cv2.imshow('gs', gs)
        #cv2.imshow('blurred', blur)
        #########
        '''
        for x in range(len(image)):
            print("hello")
        '''
        cv2.imwrite("blurred.jpeg", blur)
        #cv2.imshow('blurred', blur)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        '''
        weights = np.zeros(inputSize)

        for image in images:
            for i in range ((inputSize[0])):
                for j in range(inputSize[1]):
                    px = image.load()
                    weights[i][j] += px[j, i]

        for i in range ((inputSize[0])):
            for j in range(inputSize[1]):
                weights[i][j] /= len(images)
        print(weights)
        '''
        #Image.load(imgName)
