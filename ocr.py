import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#tesseract.exe 저장 위치


im = Image.open('C:/Users/rakk/Desktop/src/e.png') #인식할 사진위치
text = pytesseract.image_to_string(im, lang = 'jpn') #lang설정

print(text)