import cv2 as cv
import json
import os
import numpy as np
import requests as req
from io import BytesIO
from pathlib import PurePath
from PIL import Image
from pprintpp import pprint
from pytesseract import pytesseract


pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


IMG_TO_MINE = "https://mir-s3-cdn-cf.behance.net/project_modules/fs/1f25a9132072831.61a195c4d1be0.png"
res = req.get(IMG_TO_MINE)

buffer = BytesIO()
buffer.write(res.content)
img = Image.open(buffer)
img.show()
img.convert('RGB').save('skeleton_rose.jpeg')


img = cv.imread('skeleton_rose.jpeg')
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('skeleton_rose_loaded_grayscale.jpg', grayscale)
Image.open('skeleton_rose_loaded_grayscale.jpg').show()


# # increasing contrast using LAB color space: https://www.xrite.com/blog/lab-color-space
# img = cv.imread('skeleton_rose_loaded_grayscale.jpg', 1)
# # converting to LAB color space
# lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
# l_channel, a, b = cv.split(lab)
#
# # Applying CLAHE to L-channel
# # feel free to try different values for the limit and grid size:
# clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl = clahe.apply(l_channel)
#
# # merge the CLAHE enhanced L-channel with the a and b channel
# limg = cv.merge((cl,a,b))
#
# # Converting image from LAB Color model to BGR color spcae
# enhanced_img = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
#
# # Stacking the original image with the enhanced image
# result = np.hstack((img, enhanced_img))
# cv.imwrite('skeleton_rose_modified_contrast.jpg', result)
# Image.open('skeleton_rose_modified_contrast.jpg').show()



# used_threshold_value, thresholded = cv.threshold(grayscale, 50, 255, cv.THRESH_BINARY)  # TODO: Split into ranges and combine.
# used_threshold_value, thresholded = cv.threshold(grayscale, 10, 255, cv.THRESH_BINARY)  # TODO: Split into ranges and combine.
# used_threshold_value, thresholded = cv.threshold(grayscale, 10, 255, cv.THRESH_BINARY_INV)  # TODO: Split into ranges and combine.
# used_threshold_value, thresholded = cv.threshold(grayscale, 50, 255, cv.THRESH_BINARY)  # TODO: Split into ranges and combine.
# thresholded = cv.adaptiveThreshold(grayscale, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 7, 1)


thresholded = cv.adaptiveThreshold(grayscale, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 75, -1)
# used_threshold_value, thresholded = cv.threshold(grayscale, 120, 255, cv.THRESH_OTSU)
# used_threshold_value, thresholded = cv.threshold(grayscale, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
# blur = cv.GaussianBlur(grayscale,(5,5),0)
# used_threshold_value, thresholded = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# thresholded = cv.adaptiveThreshold(grayscale, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV + cv.THRESH_OTSU, 75, -1)
# print(used_threshold_value)
thresholded = np.array(thresholded)
cv.imwrite('skeleton_rose_modified_threshold.jpg', thresholded)
Image.open('skeleton_rose_modified_threshold.jpg').show()      # TODO: Re-enable after increase in contrast.



# ret, modified_image = cv2.threshold(cv2.imread('skeleton_rose.jpg'), 120, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


# modified_image.show()

# print(pytesseract.image_to_string(img))

# pprint(pytesseract.image_to_string(Image.frombytes(buffer)))



# print(pytesseract.get_languages(config=''))
# extracted_text = pytesseract.image_to_string(Image.open('skeleton_rose_modified_threshold.jpg'), lang='eng')
extracted_text = pytesseract.image_to_string(Image.open('skeleton_rose_modified_threshold.jpg'))
pprint(extracted_text.split('\n'))
# print(pytesseract.image_to_pdf_or_hocr(Image.open(IMAGE_PATH), lang='ron'))
# Image.open(IMAGE_PATH).show()


# print(page)
# try:
#     current_image_path = PurePath(WASH_IMAGES_FOLDER_PATH, f'{page}_otsu.jpg')
#     pytesseract.image_to_string(Image.open(current_image_path), lang='ron')
# except UnicodeEncodeError as e:
#     print(e)
#     Image.open(current_image_path).show()
#     raise Exception('Still error!')

"""
> pipreqs        
INFO: Not scanning for jupyter notebooks.
WARNING: requirements.txt already exists, use --force to overwrite it
> pipreqs --force
"""