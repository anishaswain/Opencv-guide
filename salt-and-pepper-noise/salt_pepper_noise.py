# USAGE
# python salt_pepper_noise.py --image cr7.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# image to be black and white (True) or not (False)
black_and_white_image = False

# proportion between amount of salt x amount of pepper
s_vs_p = 0.5

# intensity of salt and pepper noise
amount = 0.04

# load the image
if black_and_white_image:
    image = cv2.imread(args["image"], 0)
else:
    image = cv2.imread(args["image"])

out = image

# Generate Salt '1' noise
num_salt = np.ceil(amount * image.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
out[coords] = 255

# Generate Pepper '0' noise
num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
out[coords] = 0

cv2.imshow("Salt and Pepper noise", out)
cv2.waitKey(0)
