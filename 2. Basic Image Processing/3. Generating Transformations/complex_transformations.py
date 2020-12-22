# complex_tranformations.py
# Description: Applying multiple tranformations at once on one image
# Usage: python complex_tranformations.py

import cv2
import matplotlib.pyplot as plt 
import numpy as np
import random 

angles= [25, 45, 60, 120, 180, 360, -45, -90 ]
# transformations = ["rotate", "cropping", "scale", "translate", "mask", "brighten" ]
# "rotate", "cropping", "scale", "translate", "mask"
def pipeline_one(path):
    image = np.flip(cv2.imread(path), axis =2)
    # rotate
    print("ROTATING....")
    (height, width) = image.shape[:2]
    (cX, cY) = (width / 2, height / 2 )
    angle = random.choice(angles)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (width, height))
    plt.subplot(1,2,2),plt.imshow(rotated)
    plt.title("Rotated by {} Degrees".format(angle), plt.xticks([]), plt.yticks([])
    plt.show()

    # crop
    print("CROPPING...")

    # scale
    print("SCALING...")

    # translate
    print("TRANSLATING...")

    # mask
    print("MASKING...")
# "crop", "rotate", "translate", "brighten", 
def pipeline_two(path):
    
    #crop
    print("CROPPING...")
    # rotate
    print("ROTATING...")
    # translate
    print("TRANSLATING...")
    # brighten
    print("BRIGHTEN...")


    
