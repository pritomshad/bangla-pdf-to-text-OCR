# bangla-pdf-to-text-OCR
This base describes how to create a Txt document/EPUB from an image-type pdf

***These codes are only tested for Windows PCs. For Linux update the directories in ocr.py.***

*pre-requisites: 
1. Tesseract engine (https://github.com/UB-Mannheim/tesseract/wiki) - while setting up make sure to select Bangla as a language.
2. Calibre (https://calibre-ebook.com/download)

LETS GO>>>
1. After setting up Tesseract on your respective  device. Run: `pip3 install pytesseract`
2. Go to Calibre and **add your PDF** book there. Select it and click **Convert books**. Convert it to ZIP.
3. Open the directory where the ZIP is located and UnZIP the file.
4. after unzipping you can discover the Images located inside the folder.
5. you will find all the images named something like `index-1_***.jpg`.
6. paste the Python script on the directory. And run it.
7. you will find a `book.txt` document.

Edit the txt file in Google Docs and save it as EPUB.

