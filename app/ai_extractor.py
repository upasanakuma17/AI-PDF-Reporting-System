import re


def extract_invoice_data(text):

    data = {}

    # Extract invoice number
    invoice_match = re.search(
        r"Invoice Number[:\s]+(\S+)",
        text
    )

    if invoice_match:
        data["invoice_number"] = invoice_match.group(1)

    # Extract amount
    amount_match = re.search(
        r"Amount[:\s₹]+([\d,]+)",
        text
    )

    if amount_match:
        data["amount"] = amount_match.group(1)

    # Extract date
    date_match = re.search(
        r"Date[:\s]+([\d/-]+)",
        text
    )

    if date_match:
        data["date"] = date_match.group(1)

    return data