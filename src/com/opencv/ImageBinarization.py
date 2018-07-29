import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('C:/Users/hp/Desktop/portrait_practice/sampleolabill.jpg',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    cv.imwrite("C:/Users/hp/Desktop/portrait_practice/Destination_grayscale/ImagePreProcessing2Gray"+str(i)+".png",images[i]);
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
#plt.show()