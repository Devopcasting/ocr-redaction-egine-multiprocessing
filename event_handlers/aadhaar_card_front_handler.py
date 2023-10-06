import os
import time
import shutil
from watchdog.events import FileSystemEventHandler
from aadhaarcard.front import AadhaarCardFront
from helpers.write_xml import WriteXML
from ocrr_logging.ocrr_engine_log import OCRREngineLogging

class AadhaarCardFronHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        # Configure logger
        self.logger = OCRREngineLogging()

    def on_created(self, event):
        
        # Get the image path
        image_path = event.src_path

        # Check if the image file exists
        if not os.path.isfile(image_path):
            self.logger.error("Image file does not exist: %s", image_path)
            return
        
        # Get the image name
        image_file_name = os.path.basename(image_path)

        # Get the rejcted image path
        rejected_image_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\rejected_images'

        # Get the final redacted images folder path
        redacted_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\redacted_images'

        # Get xml file path
        xmls_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\redacted_images'

        # Wait for 1 second before reading the file
        while True:
            try:
                open(image_path)
                break
            except OSError:
                time.sleep(1)

        # Collect pan card informations
        collect_aadhaar_card_info_obj = AadhaarCardFront(image_path).collect_aadhaar_card_info()

        if  collect_aadhaar_card_info_obj:
            WriteXML(xmls_path, image_file_name, collect_aadhaar_card_info_obj ).writexml()
            self.logger.info(f"Writing XML file for {image_file_name}")

            # Move the image to redacted folder
            shutil.move(image_path,  os.path.join(redacted_path, image_file_name))
            self.logger.info(f"Aadhaar card image {image_file_name} moved to redacted folder")         
        else:
            # Move the image to rejected folder
            shutil.move(image_path,  os.path.join(rejected_image_path, image_file_name))
            self.logger.error("AADERR001")