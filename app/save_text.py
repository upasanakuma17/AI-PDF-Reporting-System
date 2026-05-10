from datetime import datetime

def save_text_to_file(text):

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    # Unique filename
    output_file = f"output/extracted_text_{timestamp}.txt"

    # Save file
    with open(output_file, "w", encoding="utf-8") as file:

        file.write(text)

    print(f"\nText File Saved: {output_file}")