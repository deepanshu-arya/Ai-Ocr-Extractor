import pytesseract
from pdf2image import convert_from_path

def extract_pdf(file_path):
    images = convert_from_path(file_path)

    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)

    return text