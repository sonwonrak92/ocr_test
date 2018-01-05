import pytesseract
from PIL import Image
import numpy as np


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#tesseract.exe 저장 위치
im = Image.open('C:/Users/rakk/Desktop/src/plate_th.jpg') #인식할 사진위치

text = pytesseract.image_to_string(im, lang='kor') #lang설정 [kor =한글 , jpn = 일본어, eng = 영어]

print(text)
# with open('magic.txt', mode='w') as file:
#     file.write(text)
