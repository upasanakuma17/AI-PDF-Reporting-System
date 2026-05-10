import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app.extractor import extract_text_from_pdf
from app.save_text import save_text_to_file
from app.pdf_generator import generate_pdf_report


class PDFHandler(FileSystemEventHandler):

    def on_created(self, event):

        # Ignore folders
        if event.is_directory:
            return

        # Check if file is PDF
        if event.src_path.endswith(".pdf"):

            print(f"\nNew PDF detected: {event.src_path}")

            # Extract text
            text = extract_text_from_pdf(event.src_path)

            # Save extracted text
            save_text_to_file(text)

            # Generate PDF report
            generate_pdf_report(text)

            print("\nProcessing Completed!")


# Folder to monitor
folder_to_watch = "input/pdfs"

# Create event handler
event_handler = PDFHandler()

# Create observer
observer = Observer()

# Connect observer to folder
observer.schedule(event_handler, folder_to_watch, recursive=False)

# Start monitoring
observer.start()

print(f"Watching folder: {folder_to_watch}")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()