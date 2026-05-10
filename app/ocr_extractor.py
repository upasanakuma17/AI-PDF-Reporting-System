import fitz
import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_with_ocr(pdf_path):

    # Open PDF
    doc = fitz.open(pdf_path)

    full_text = ""

    # Read every page
    for page_num in range(len(doc)):

        page = doc[page_num]

        # Convert page to image
        pix = page.get_pixmap()

        image_path = f"output/page_{page_num}.png"

        pix.save(image_path)

        # Open image
        image = Image.open(image_path)

        # OCR extraction
        text = pytesseract.image_to_string(image)

        full_text += text

    return full_text