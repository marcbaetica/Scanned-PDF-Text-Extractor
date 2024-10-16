import os
import cv2 as cv
import numpy as np
import shutil
from pathlib import PurePath
from PIL import Image


image = 'page_20.jpg'
IMAGES_FOLDER = 'extracted_images'
CUT_IMAGES_FOLDER = 'cut_images'
CUT_IMAGES_FOLDER_PATH = PurePath(CUT_IMAGES_FOLDER)


# delete folder beforehand
if CUT_IMAGES_FOLDER in os.listdir('.'):
    shutil.rmtree(CUT_IMAGES_FOLDER)


print(os.listdir('.'))
if not CUT_IMAGES_FOLDER in os.listdir('.'):
    os.mkdir(CUT_IMAGES_FOLDER_PATH)
    for image in os.listdir(IMAGES_FOLDER):
        shutil.copy2(PurePath(IMAGES_FOLDER, image), CUT_IMAGES_FOLDER_PATH)


for image in os.listdir(CUT_IMAGES_FOLDER):
    (left, upper, right, lower) = (350, 0, 2866, 1870)  # original 2866x2024
    image_path = PurePath(CUT_IMAGES_FOLDER_PATH, image)
    with Image.open(image_path) as im:
        im_crop = im.crop((left, upper, right, lower))
        im_crop.save(f'{CUT_IMAGES_FOLDER}/{image}', 'JPEG')



    # print(image_path)
    # print(str(image_path))
    # img = cv.imread(str(image_path))
    # grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # used_threshold_value, thresholded = cv.threshold(grayscale, 0, 255, cv.THRESH_OTSU)
    # print(used_threshold_value)
    # # thresholded = np.array(thresholded)
    # cv.imwrite(f'cut_images\{image.split(".")[0]}_otsu.jpg', thresholded)
    # bbox = cv.boundingRect(thresholded)
    # x, y, w, h = bbox
    # print(bbox)
    # foreground = img[y:y + h, x:x + w]
    # cv.imwrite(f'cut_images\{image.split(".")[0]}_foreground.png', foreground)

