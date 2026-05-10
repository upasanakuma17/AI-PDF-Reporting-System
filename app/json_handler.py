import json
from datetime import datetime


def create_json_data(extracted_text):

    data = {
        "generated_on": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "total_characters": len(extracted_text),
        "total_words": len(extracted_text.split()),
        "content_preview": extracted_text[:500],
        "full_text": extracted_text
    }

    return data


def save_json_file(data):

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    output_file = f"output/report_data_{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"JSON File Saved: {output_file}")