# random_geometrical_tranformations.py
# Description: Applying multiple tranformations at once on one image
# Usage: python rand_geometriccal_tranformations.py
# Copyright() rndMemex@cantab.net

import argparse
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import random 

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help = 'Use -i flag with path to image as argument')
ap.add_argument('-s', '--save', required=True, help = 'Use -s flag with path to output as argument')
args = vars(ap.parse_args())

# Loading an image
image = cv2.imread(args["image"]) #B R G
output = args["save"]
cv2.imshow('Input Image', image)
cv2.waitKey(0)
image = np.flip(image, axis =2)
angles= [25, 45, 60, 120, 180, 360, -45, -90 ]
(height, width) = image.shape[:2]

def saving_image(image, output, image_name):
    #save your image to output path using opencv
    path = output
    cv2.imwrite(os.path.join(path,image_name), image)
    cv2.waitKey(0)

# function block
def crop(image, output):
    #crop
    print("CROPPING...")
    cropped = image[85:250, 85:220] # h, w 
    plt.figure(figsize=(20,10))
    plt.subplot(2,2,2),plt.imshow(cropped)
    plt.title('Cropped'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(cropped, output, 'cropped_image.jpg')

def rotate(image, output):
    # rotate stuff 
    (height, width) = image.shape[:2]
    (cX, cY) = (width / 2, height / 2 )
    angle = random.choice(angles)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (width, height))
    plt.subplot(1,2,2),plt.imshow(rotated)
    plt.title("Rotated by {} Degrees".format(angle)), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(rotate, output, 'rotated_image.jpg')


def bright(image, output):
    # add stuff
    print("BRIGHTEN...")
    M = np.ones(image.shape, dtype = "uint8") * 100
    added = cv2.add(image, M)

    plt.figure(figsize=(20,10))
    plt.subplot(2,2,1),plt.imshow(image)
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(added)
    plt.title('Added'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(added, output, 'brghtened_image.jpg')

def substract(image, output):
    #  substract stuff
    M = np.ones(image.shape, dtype = "uint8") * 50
    subtracted = cv2.subtract(image, M)
    plt.figure(figsize=(20,10))
    plt.subplot(2,2,2),plt.imshow(subtracted)
    plt.title('Subtracted'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(substract, output, 'darkened_image.jpg')


def translate(image, output):
    # translate stuff
    # translate
    print("TRANSLATING...")
    M = np.float32([[1, 0, 25], [0, 1, 50]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    plt.figure(figsize=(20,10))
    plt.subplot(1,2,2),plt.imshow(shifted)
    plt.title('Translated'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(shifted, output, 'translated_image.jpg')

def scale(image, output):
    # scale stuff
    print("SCALING...")
    resized_width = 1280

    # calculating ratio of new image to old image
    ratio = resized_width / width
    dim = (resized_width, int(height * ratio))

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    print(f'Original shape: {image.shape} vs Resized shape {resized.shape}')
    plt.figure(figsize=(20,10))
    plt.subplot(1,2,1), plt.imshow(image) 
    plt.title('Original')
    plt.subplot(1,2,2), plt.imshow(resized)
    plt.title('Resized')
    plt.show()
    saving_image(resized, output, 'scaled_image.jpg')

def flipOne(image, output):
    # flip stuff
    print("FLIPPING HORIZONTALLY...")
    # flip the image horizontally
    hflipped = cv2.flip(image, 1)


    plt.figure(figsize=(20,10))
    plt.subplot(2,2,2),plt.imshow(hflipped)
    plt.title('Flipped Horizontally'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(hflipped, output, 'flipedX_image.jpg')

def flipTwo(image, output):
    print("FLIPPING VERTICALLY...")
    # flip the image vertically
    vflipped = cv2.flip(image, 0)    
    plt.figure(figsize=(20,10))
    plt.subplot(2,2,3),plt.imshow(vflipped)
    plt.title('Flipped Vertically'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(vflipped, output, 'flippedTwo_image.jpg')   

def flipThree(image, output):
    print("FLIPPING HORIZONTALLY & VERTICALLY...")
    # flip the image along both axes
    hvflipped = cv2.flip(image, -1)
    plt.figure(figsize=(20,10))
    plt.subplot(2,2,4),plt.imshow(hvflipped)
    plt.title('Flipped Horizontally & Vertically'), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(hvflipped, output, 'flippedThree_image.jpg')

def mask(image, output):
    # mask stuff
    print("MASKING...")

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask, (145, 200), 100, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    plt.subplot(1,2,2),plt.imshow(masked)
    plt.title("Masked"), plt.xticks([]), plt.yticks([])
    plt.show()
    saving_image(masked, output, 'masked_image.jpg')


transformationsSwitcher = {
    1: crop, 
    2: rotate, 
    3: bright, 
    4: substract, 
    5: translate, 
    6: scale, 
    7: flipOne,
    8: flipTwo,
    9: flipThree, 
    10: mask
}

# invoke switch block 
for i in range (1, 11):
    num = random.randint(1, 10)
    print("{}th Image".format(1))
    print("random transformation: {}".format(num))
    transformationsSwitcher[num](image, output)








