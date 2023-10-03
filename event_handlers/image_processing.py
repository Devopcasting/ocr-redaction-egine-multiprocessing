import os
import time
from watchdog.events import FileSystemEventHandler
from helpers.process_image import ProcessJPEGImages
from ocrr_logging.ocrr_engine_log import OCRREngineLogging


class ImageProcessingEnventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Configure logger
        config = OCRREngineLogging()
        logger = config.configure_logger()
        
        # Uploaded image path
        image_path = event.src_path
        
        # Set the process image path
        processed_image_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\processed_images'

        # Get the file name
        file_name = os.path.basename(image_path)

        # Wait for 1 second before reading the file
        while True:
            try:
                open(image_path)
                break
            except OSError:
                time.sleep(1)

        # Process the image
        process_image_obj = ProcessJPEGImages(image_path, processed_image_path)
        if process_image_obj.processed_image():
            logger.info(f"Image {file_name} processed successfully")
        else:
            logger.error(f"Error Code : ERR001")