import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import randint

class circleCenterInView:
    def __init__(self, filename):
        self.filename = filename

    def inView(self):
        mask = cv2.imread(self.filename)
        #plt.imshow(mask, cmap='gray')
        #plt.show()

        gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.imshow('contour', thresh)

        cnts = imutils.grab_contours(cnts)
        #print(cnts)

        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            #print((cX,cY))
            # draw the center of the shape on the image
            cv2.circle(mask, (cX, cY), 7, (0, 0, 255), -1)

            # show the image
            plt.imshow(mask, cmap='gray')
            plt.show()
        return cX,cY
    def approximater(self):

        pt1,pt2,pt3 = self.threePts()
        x1=pt1[0][0]
        y1=pt1[0][1]
        x2 = pt2[0][0]
        y2 = pt2[0][1]
        x3 = pt3[0][0]
        y3 = pt3[0][1]

        x12 = x1 - x2
        x13 = x1 - x3

        y12 = y1 - y2
        y13 = y1 - y3

        y31 = y3 - y1
        y21 = y2 - y1

        x31 = x3 - x1
        x21 = x2 - x1

        # x1^2 - x3^2
        sx13 = pow(x1, 2) - pow(x3, 2)

        # y1^2 - y3^2
        sy13 = pow(y1, 2) - pow(y3, 2)

        sx21 = pow(x2, 2) - pow(x1, 2)
        sy21 = pow(y2, 2) - pow(y1, 2)

        f = (((sx13) * (x12) + (sy13) * (x12) + (sx21) * (x13) + (sy21) * (x13)) // (2 *((y31) * (x12) - (y21) * (x13))))

        g = (((sx13) * (y12) + (sy13) * (y12) + (sx21) * (y13) + (sy21) * (y13)) // (2 * ((x31) * (y12) - (x21) * (y13))))

        c = (-pow(x1, 2) - pow(y1, 2) - 2 * g * x1 - 2 * f * y1)

        # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
        # where center is (h = -g, k = -f) and
        h = -g
        k = -f

        #sqr_of_r = h * h + k * k - c;
        #r = round(sqrt(sqr_of_r), 5);
        #print("Radius",r)

        #print("Center = (", h, ", ", k, ")")
        return h,k



    def threePts(self):
        mask = cv2.imread(self.filename)
        # plt.imshow(mask, cmap='gray')
        # plt.show()

        gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.imshow('contour', thresh)

        cnts = imutils.grab_contours(cnts)
        #print(cnts)
        r1 = randint(int(len(cnts[0])/2),len(cnts[0])-1)
        p1 = cnts[0][r1]

        r2 = randint(int(len(cnts[0])/2),len(cnts[0])-1)
        while r2==r1:
            r2 = randint(int(len(cnts[0])/2), len(cnts[0])-1)
        p2 = cnts[0][r2]

        r3 = randint(int(len(cnts[0])/2), len(cnts[0])-1)
        while r3 == r1 or r3 == r2:
            r3 = randint(int(len(cnts[0])/2), len(cnts[0])-1)
        p3 = cnts[0][r3]
        #print(p1,p2,p3)
        return p1,p2,p3


