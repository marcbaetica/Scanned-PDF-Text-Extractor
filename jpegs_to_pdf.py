import os
import sys

import img2pdf
from pathlib import PurePath
from PIL import Image


JPEG_PAGES_FOLDER = PurePath('split_pages')
PDF_FILE_NAME = 'Sarbu, Oprea - Plante vasculare Determinator SINGLE PAGE.pdf'
PDF_FILE_PATH = PurePath(PDF_FILE_NAME)


images = os.listdir(JPEG_PAGES_FOLDER)
print(images)
print(len(images))

images.sort(key=lambda x: int(x.split('.')[0]))
images.pop(0)
print(images)


def test_alphabetical_sorting(images_list):
    for index in range(len(images_list)-1):
        if get_page_number(images_list[index]) >= get_page_number(images_list[index+1]):
            raise AssertionError(f'{images_list[index]} is larger or equal to the next item {images_list[index+1]}')


def get_page_number(file_name):
    return int(file_name.split('.')[0])


test_alphabetical_sorting(images)

images = [str(PurePath(JPEG_PAGES_FOLDER, image)) for image in images]




img = Image.open('842.jpg')
img.save('842_10.jpg', 'JPEG', quality=10)
img.save('842_5.jpg', 'JPEG', quality=5)
img.save('842_1.jpg', 'JPEG', quality=1)


print(os.path.getsize('842.jpg'))       # 488199 bytes
print(os.path.getsize('842_10.jpg'))    # 147347 bytes
print(os.path.getsize('842_5.jpg'))     # 108016 bytes
print(os.path.getsize('842_1.jpg'))     # 88076 bytes


from io import BytesIO


buffer = BytesIO()
images_data = []
for image_path in images:
    img = Image.open(image_path)
    img.save(buffer, 'JPEG', quality=100)
    images_data.append(buffer.getvalue())
    # Flush out the stream. https://stackoverflow.com/questions/59026837/how-to-flush-python-io-stream
    buffer.seek(0)      # change the position of the stream to its start
    buffer.truncate(0)  # resize the stream to 0. Not passing a value defaults to the current position
    # https://stackoverflow.com/questions/26827055/python-how-to-get-bytesio-allocated-memory-length
    # Or you could be nasty and call __sizeof__() directly
    # (which is like sys.getsizeof() but without garbage collector overhead applicable to the object).
    # Also, buffer.tell() returns the current stream position.
    print({image_path}, len(buffer.getvalue()), buffer.getbuffer().nbytes, sys.getsizeof(buffer),
          buffer.tell(), len(images_data), len(images_data[-1]), sum([len(data) for data in images_data]))
    """
    BEFORE FLUSHING:
    {'split_pages\\1.jpg'} 60473 60473 60586 60473 1 60473 60473
    {'split_pages\\2.jpg'} 102155 102155 102268 102155 2 102155 162628
    {'split_pages\\3.jpg'} 151351 151351 151464 151351 3 151351 313979
    {'split_pages\\4.jpg'} 233532 233532 233645 233532 4 233532 547511
    {'split_pages\\5.jpg'} 388109 388109 388222 388109 5 388109 935620
    {'split_pages\\6.jpg'} 534400 534400 534513 534400 6 534400 1470020

    AFTER FLUSHING:
    {'split_pages\\1.jpg'} 0 0 114 0 1 60473 60473
    {'split_pages\\2.jpg'} 0 0 114 0 2 41682 102155
    {'split_pages\\3.jpg'} 0 0 114 0 3 49196 151351
    {'split_pages\\4.jpg'} 0 0 114 0 4 82181 233532
    {'split_pages\\5.jpg'} 0 0 114 0 5 154577 388109
    {'split_pages\\6.jpg'} 0 0 114 0 6 146291 534400
    """


with open(PDF_FILE_NAME, "wb") as f:
    pdf_data = img2pdf.convert(images_data)
    f.write(pdf_data)
