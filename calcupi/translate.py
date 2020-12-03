from PIL import Image
import pytesseract

file = Image.open("_img/jpg.png")
text = pytesseract.image_to_string(file, lang='eng')

print(text)

