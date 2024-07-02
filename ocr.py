import os
import pytesseract
from PIL import Image

# Set TESSDATA_PREFIX environment variable in the script
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
# Path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

full_book = ''
book_name = input("Book name: ")
pages = int(input("Page numbers in your book: "))
filetype = input("File type of the images (i.e. jpg, png): ")

for i in range(1,pages+1):
    image = Image.open(str(i) + '_1.' + filetype)
    text = pytesseract.image_to_string(image, lang='ben')
    full_book = full_book + '\n' + text
    print("page "+str(i)+" done.")


# Write the extracted text to a text file
with open((book_name + '.txt'), 'w', encoding='utf-8') as file:
    file.write(full_book)
