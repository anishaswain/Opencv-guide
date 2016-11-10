#import all dependencies
import numpy as numpy
import cv2

#reads the image, 0 as black and white , 1 as colored 
img = cv2.imread("basketball2.png",1)

#resizable window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#shows image
cv2.imshow('image',img)

#writes image as name 123.png
cv2.imwrite("123.png",img)

#waitKey takes parameter as millisecond till which the function will run
#if the parameter is 0 then, the functions run for infinite time
cv2.waitKey(0)

#used for destroying the opend window
#can use destroyWindow('windowname') for destroying particularly one wondow
cv2.destroyAllWindows()
