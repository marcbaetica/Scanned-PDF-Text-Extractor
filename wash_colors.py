import os
import cv2 as cv
import numpy as np
import shutil
from pathlib import PurePath
from PIL import Image


# image = 'page_421.jpg'
image = 'page_21.jpg'
SPLIT_IMAGES_FOLDER = 'split_pages'
SPLIT_IMAGES_FOLDER_PATH = PurePath(SPLIT_IMAGES_FOLDER)
WASH_IMAGES_FOLDER = 'washed_images'
WASH_IMAGES_FOLDER_PATH = PurePath(WASH_IMAGES_FOLDER)


# delete folder beforehand
if WASH_IMAGES_FOLDER in os.listdir('.'):
    shutil.rmtree(WASH_IMAGES_FOLDER_PATH)

#
print(os.listdir('.'))
if not WASH_IMAGES_FOLDER in os.listdir('.'):
    os.mkdir(WASH_IMAGES_FOLDER_PATH)
    # for image in os.listdir(SPLIT_IMAGES_FOLDER_PATH):
    #     shutil.copy2(PurePath(SPLIT_IMAGES_FOLDER_PATH, image), WASH_IMAGES_FOLDER_PATH)


for image in os.listdir(SPLIT_IMAGES_FOLDER_PATH):
    image_path = PurePath(SPLIT_IMAGES_FOLDER_PATH, image)
    # print(image_path)
    # print(str(image_path))
    img = cv.imread(str(image_path))
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    used_threshold_value, thresholded = cv.threshold(grayscale, 0, 255, cv.THRESH_OTSU)
    # print(used_threshold_value)
    thresholded = np.array(thresholded)
    cv.imwrite(f'{WASH_IMAGES_FOLDER_PATH}\{image.split(".")[0]}_otsu.jpg', thresholded)
    # bbox = cv.boundingRect(thresholded)
    # x, y, w, h = bbox
    # print(bbox)
    # foreground = img[y:y + h, x:x + w]
    # cv.imwrite(f'cut_images\{image.split(".")[0]}_foreground.png', foreground)

