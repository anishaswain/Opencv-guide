# USAGE
# python detect_edge_canny.py --image lebron.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

canny_edges_image = cv2.Canny(image, 100, 200)

cv2.imshow("Canny edge detection", canny_edges_image)
cv2.waitKey(0)
