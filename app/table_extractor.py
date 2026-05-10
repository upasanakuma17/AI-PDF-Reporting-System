import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path):

    all_tables = []

    # Open PDF
    with pdfplumber.open(pdf_path) as pdf:

        # Read every page
        for page in pdf.pages:

            # Extract tables from page
            tables = page.extract_tables()

            # Add tables into list
            for table in tables:

                # Convert table into DataFrame
                df = pd.DataFrame(table)

                all_tables.append(df)

    return all_tables