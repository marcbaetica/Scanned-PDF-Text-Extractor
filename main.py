import os
from pathlib import PurePath
from pdf2image import convert_from_path


PDF_FOLDER = 'pdf_scan'

PDF_PATH = PurePath(PDF_FOLDER, os.listdir(PDF_FOLDER)[1])

print(PDF_PATH)
pages = convert_from_path(PDF_PATH)

# Save each page as a JPEG file using Pillow

print(os.listdir('.'))
IMAGES_FOLDER = 'extracted_images'
if not IMAGES_FOLDER in os.listdir('.'):
	os.mkdir(IMAGES_FOLDER)

for i, page in enumerate(pages):
	img_path = PurePath(IMAGES_FOLDER, f'page_{i}.jpg')
	page.save(img_path, 'JPEG')
	print(i, page)
	"""
	0 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FCFF7EF0A0>
	1 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FCFF7EF0D0>
	2 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523D00>
	3 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523FD0>
	4 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523FA0>
	5 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523F70>
	6 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523BE0>
	7 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523C10>
	8 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523A60>
	9 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523A00>
	10 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC825239A0>
	11 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523970>
	12 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523850>
	13 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523BB0>
	14 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82523D30>
	15 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82531040>
	16 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC825310A0>
	17 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC825310D0>
	18 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82531100>
	19 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82531130>
	20 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82531160>
	21 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC82531190>
	22 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x1FC825311C0>
	...
	648 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365910>
	649 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365940>
	650 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365970>
	651 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E3659A0>
	652 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E3659D0>
	653 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365A00>
	654 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365A30>
	655 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365A60>
	656 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365A90>
	657 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365AC0>
	658 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365AF0>
	659 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365B20>
	660 <PIL.PpmImagePlugin.PpmImageFile image mode=RGB size=2866x2024 at 0x2016E365B50>
	"""