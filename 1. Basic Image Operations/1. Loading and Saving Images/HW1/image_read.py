# usage: python image_read.py 
# description: function that reads in an image using either the matplotlib or CV2 and shows it in this notebook using matplotlib
# Copyright rndMemex@cantab.net

import cv2
import matplotlib.pyplot as plt
import numpy as np

def read_and_show(path, cmap = None, fig_size = (10, 10)):
    # read an image using opencv
    image = cv2.imread(path) # B R G 
    # show image using matplotlib, flip it first
    image = np.flip(image, axis = 2)
    image.shape
    fig, ax = plt.subplots(figsize =fig_size)
    ax.imshow(image, cmap = cmap)
    ax.axis('on')
    plt.show()


# test
read_and_show('../img/robotic_arm.jpg')   
