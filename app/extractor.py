import fitz
def extract_text_from_pdf(pdf_path):

    # Open the PDF file
    doc = fitz.open(pdf_path)

    full_text = ""

    # Read all pages
    for page in doc:

        # Extract text from page
        text = page.get_text()

        # Add page text into full_text
        full_text += text

    return full_text