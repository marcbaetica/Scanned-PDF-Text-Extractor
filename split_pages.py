import os
import cv2 as cv
import numpy as np
import shutil
from pathlib import PurePath
from PIL import Image


# image = 'page_421.jpg'
image = 'page_21.jpg'
CUT_IMAGES_FOLDER = 'cut_images'
CUT_IMAGES_FOLDER_PATH = PurePath(CUT_IMAGES_FOLDER)
SPLIT_IMAGES_FOLDER = 'split_pages'
SPLIT_IMAGES_FOLDER_PATH = PurePath(SPLIT_IMAGES_FOLDER)

# delete folder beforehand
if SPLIT_IMAGES_FOLDER in os.listdir('.'):
    shutil.rmtree(SPLIT_IMAGES_FOLDER_PATH)


print(os.listdir('.'))
if not SPLIT_IMAGES_FOLDER in os.listdir('.'):
    os.mkdir(SPLIT_IMAGES_FOLDER_PATH)
    for image in os.listdir(CUT_IMAGES_FOLDER_PATH):
        shutil.copy2(PurePath(CUT_IMAGES_FOLDER_PATH, image), SPLIT_IMAGES_FOLDER_PATH)


for image in os.listdir(SPLIT_IMAGES_FOLDER_PATH):
    page_number_left = int(image.split(".")[0].split("_")[1])*2
    page_number_right = int(image.split(".")[0].split("_")[1])*2+1
    (l_left, l_upper, l_right, l_lower) = (0, 0, 1320, 1870)  # original 2516x1870
    image_path = PurePath(CUT_IMAGES_FOLDER_PATH, image)
    with Image.open(image_path) as im:
        im_crop = im.crop((l_left, l_upper, l_right, l_lower))
        im_crop.save(f'{SPLIT_IMAGES_FOLDER_PATH}/{page_number_left}.jpg', 'JPEG')
    (r_left, r_upper, r_right, r_lower) = (1320, 0, 2516, 1870)  # original 2516x1870
    image_path = PurePath(CUT_IMAGES_FOLDER_PATH, image)
    with Image.open(image_path) as im:
        im_crop = im.crop((r_left, r_upper, r_right, r_lower))
        im_crop.save(f'{SPLIT_IMAGES_FOLDER_PATH}/{page_number_right}.jpg', 'JPEG')
    os.remove(f'{SPLIT_IMAGES_FOLDER_PATH}/{image}')
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

