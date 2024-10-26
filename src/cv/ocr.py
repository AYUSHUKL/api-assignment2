import easyocr

def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    return reader.readtext(image_path, detail=0)
