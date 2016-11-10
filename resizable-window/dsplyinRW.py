#import all dependencies
import numpy as numpy
import cv2


#Reads the image from current foldder
img = cv2.imread("basketball2.png",1)

#it creates a resizeable window by WINDOW_NORMAL
#by default it is WINDOW_AUTOSIZE
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#show the read image as window name 'image'
#if want more than one window write their names separated by comma inside ''
cv2.imshow('image',img)

#waitKey takes parameter as millisecond till which the function will run
#if the parameter is 0 then, the functions run for infinite time
cv2.waitKey(0)

#used for destroying the opend window
#can use destroyWindow('windowname') for destroying particularly one wondow
cv2.destroyAllWindows()
