import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

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
        cnts = imutils.grab_contours(cnts)

        for c in cnts:
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            print((cX,cY))
            # draw the center of the shape on the image
            cv2.circle(mask, (cX, cY), 7, (0, 0, 255), -1)

            # show the image
            plt.imshow(mask, cmap='gray')
            plt.show()
