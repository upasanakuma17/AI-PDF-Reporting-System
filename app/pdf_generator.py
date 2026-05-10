from fpdf import FPDF
from datetime import datetime

def generate_pdf_report(extracted_text):

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # File name
    output_file = f"output/report_{timestamp}.pdf"

    # Current readable date/time
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Calculate statistics
    total_characters = len(extracted_text)
    total_words = len(extracted_text.split())

    # Create PDF
    pdf = FPDF()

    # Add page
    pdf.add_page()

    # -----------------------------
    # TITLE
    # -----------------------------
    pdf.set_font("Arial", style='B', size=18)

    pdf.cell(200, 10, "PDF Analysis Report", ln=True, align='C')

    # Space
    pdf.ln(10)

    # -----------------------------
    # DATE SECTION
    # -----------------------------
    pdf.set_font("Arial", style='B', size=12)

    pdf.cell(200, 10, f"Generated On: {current_time}", ln=True)

    # Line separator
    pdf.cell(200, 10, "-" * 70, ln=True)

    # -----------------------------
    # EXTRACTED CONTENT TITLE
    # -----------------------------
    pdf.set_font("Arial", style='B', size=14)

    pdf.cell(200, 10, "Extracted Content:", ln=True)

    # -----------------------------
    # CONTENT
    # -----------------------------
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, extracted_text)

    # Space
    pdf.ln(5)

    # Line separator
    pdf.cell(200, 10, "-" * 70, ln=True)

    # -----------------------------
    # STATISTICS SECTION
    # -----------------------------
    pdf.set_font("Arial", style='B', size=14)

    pdf.cell(200, 10, "Document Statistics", ln=True)

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, f"Total Characters: {total_characters}", ln=True)

    pdf.cell(200, 10, f"Total Words: {total_words}", ln=True)

    # Save PDF
    pdf.output(output_file)

    print(f"\nProfessional PDF Report Saved: {output_file}")