import os
import cv2
import imutils


def modify_images(filenames):
    images = []
    for i in range(len(filenames)):
        images.append(cv2.imread(filenames[i]))
    # resize images for program work fast but when panorama more images will wrong
    # for i in range(len(images)):
    #     images[i] = imutils.resize(images[i], width=400)

    # for i in range(len(images)):
    #     images[i] = imutils.resize(images[i], height=400)

    return images
