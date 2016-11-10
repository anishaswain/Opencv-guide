#import all dependencies
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Reads the image from current foldder
img = cv2.imread('messi.jpg',0)

#shows image & maps image as gray 
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([]) 

#plots image
plt.show()
