import streamlit as st

from app.extractor import extract_text_from_pdf
from app.ocr_extractor import extract_text_with_ocr
from app.llm_extractor import extract_data_with_llm
from app.pdf_generator import generate_pdf_report
from app.json_handler import create_json_data


# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI PDF Reporting System",
    page_icon="📄",
    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------

st.title("📄 AI-Powered PDF Reporting System")

st.markdown(
    """
This system can:

- Extract text from PDFs
- Read scanned PDFs using OCR
- Generate structured JSON
- Perform AI-based extraction using LLMs
- Generate automated reports
"""
)

st.divider()

# --------------------------------
# FILE UPLOAD
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

# --------------------------------
# PROCESS PDF
# --------------------------------

if uploaded_file is not None:

    st.success("PDF Uploaded Successfully!")

    pdf_path = f"input/pdfs/{uploaded_file.name}"

    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.read())

    st.info("Processing PDF...")

    # ----------------------------
    # TEXT EXTRACTION
    # ----------------------------

    extracted_text = extract_text_from_pdf(pdf_path)

    # ----------------------------
    # OCR EXTRACTION
    # ----------------------------

    ocr_text = extract_text_with_ocr(pdf_path)

    # ----------------------------
    # SELECT BEST TEXT
    # ----------------------------

    final_text = extracted_text

    if len(final_text.strip()) < 50:
        final_text = ocr_text

    # ----------------------------
    # JSON GENERATION
    # ----------------------------

    json_data = create_json_data(final_text)

    # ----------------------------
    # AI EXTRACTION
    # ----------------------------

    ai_result = extract_data_with_llm(final_text)

    # ----------------------------
    # GENERATE PDF REPORT
    # ----------------------------

    generate_pdf_report(final_text)

    # --------------------------------
    # LAYOUT COLUMNS
    # --------------------------------

    col1, col2 = st.columns(2)

    # LEFT SIDE
    with col1:

        st.subheader("📑 Extracted Text")

        st.text_area(
            "PDF Content",
            final_text,
            height=400
        )

    # RIGHT SIDE
    with col2:

        st.subheader("🧠 AI Extracted Data")

        st.code(ai_result, language="json")

        st.subheader("📦 Generated JSON")

        st.json(json_data)

    st.success("Report Generated Successfully!")
    
with open("output/final_report.pdf", "rb") as file:
    st.download_button(
        label="Download PDF Report",
        data=file,
        file_name="final_report.pdf",
        mime="application/pdf"
    )