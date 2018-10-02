import cv2
import numpy as np
 
img = cv2.imread('leo.jpg',1)

###########################################################################################
################################## GAUSSIAN NOISE #########################################
###########################################################################################

row,col,ch= img.shape
mean = 0
gauss = np.random.normal(mean,1,(row,col,ch))
gauss = gauss.reshape(row,col,ch)
noisy = img + gauss

print(noisy.shape)


cv2.imshow('image',noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()



 