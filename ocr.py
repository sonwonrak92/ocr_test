import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#tesseract.exe 저장 위치


im = Image.open('d.png') #인식사진위치
text = pytesseract.image_to_string(im, lang = 'kor') #lang설정

print(text)