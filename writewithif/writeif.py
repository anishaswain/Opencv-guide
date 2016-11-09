import numpy as numpy
import cv2
img = cv2.imread("basketball2.png",1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
