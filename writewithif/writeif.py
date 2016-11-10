#import all dependencies
import numpy as numpy
import cv2

#reads image
img = cv2.imread("basketball2.png",1)

#resixable window creation
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#showing images
cv2.imshow('image',img)

#declarinf variable k which is waitKey stroke
k = cv2.waitKey(0)

#if k is presed as 27 or esc then it will destroy all windows
if k == 27:
    cv2.destroyAllWindows()

#else if waitkey is pressed as 's' then it writes the image as messigray.png 
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
