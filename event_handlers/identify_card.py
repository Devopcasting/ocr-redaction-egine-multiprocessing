import os
import time
import shutil
import pytesseract
from watchdog.events import FileSystemEventHandler
from helpers.process_text import CleanText
from helpers.identify_pan_card import IdentifyPanCard
from ocrr_logging.ocrr_engine_log import OCRREngineLogging

class IdentifyCard(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        # Configure logger
        self.logger = OCRREngineLogging()

    def on_created(self, event):
        # Get image path
        image_path = event.src_path

        # Get file name
        image_file_name = os.path.basename(image_path)

        # Pan card Pattern1 path
        pan_card_p1_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\pan_card\pattern1'

        # Pan card Pattern2 path
        pan_card_p2_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\pan_card\pattern2'

        # Wait for 1 second before reading the file
        while True:
            try:
                open(image_path)
                break
            except OSError:
                time.sleep(1)

        # Configure tesseract
        tesseract_config = r'-l eng --oem 3 --psm 6'
    
        # Get the text in Dict from image
        data_text = pytesseract.image_to_string(image_path, output_type=pytesseract.Output.DICT,config=tesseract_config)
        clean_text = CleanText(data_text).clean_text()

        # Check for Pan card
        pan_card = IdentifyPanCard(clean_text)
        if pan_card.check_pan_card():
            if pan_card.identify_pan_card_pattern_1():
                self.logger.info(f"Pan card {image_file_name} is of pattern 1")
                shutil.move(image_path, os.path.join(pan_card_p1_path, image_file_name))
            else:
                self.logger.info(f"Pan card {image_file_name} is of pattern 2")
                shutil.move(image_path, os.path.join(pan_card_p2_path, image_file_name))

    