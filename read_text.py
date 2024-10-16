import os
from pathlib import PurePath
from PIL import Image
from pytesseract import pytesseract


# image = '21_otsu.jpg'
# image = '421_otsu.jpg'
image = '842_otsu.jpg'
WASH_IMAGES_FOLDER = 'washed_images'
WASH_IMAGES_FOLDER_PATH = PurePath(WASH_IMAGES_FOLDER)
IMAGE_PATH = PurePath(WASH_IMAGES_FOLDER_PATH, image)
PARSED_TEXT_FILE = 'extracted_text.txt'


pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.get_languages(config=''))
# print(pytesseract.image_to_string(Image.open(IMAGE_PATH), lang='ron'))
# print(pytesseract.image_to_pdf_or_hocr(Image.open(IMAGE_PATH), lang='ron'))
# Image.open(IMAGE_PATH).show()


if PARSED_TEXT_FILE in os.listdir('.'):
    os.remove(PARSED_TEXT_FILE)

with open(PARSED_TEXT_FILE, 'w', encoding='utf-8') as f:
    for page in range(len(os.listdir(WASH_IMAGES_FOLDER_PATH))):
        print(page)
        f.write(f'\n\n\n\n------------------------------- Page {page} Start -------------------------------\n\n\n\n')
        try:
            current_image_path = PurePath(WASH_IMAGES_FOLDER_PATH, f'{page}_otsu.jpg')
            f.write(pytesseract.image_to_string(Image.open(current_image_path), lang='ron'))
        except UnicodeEncodeError as e:
            print(e)
            Image.open(current_image_path).show()
            raise Exception('Still error!')
        f.write(f'\n\n\n\n-------------------------------- Page {page} End --------------------------------\n\n\n\n')
