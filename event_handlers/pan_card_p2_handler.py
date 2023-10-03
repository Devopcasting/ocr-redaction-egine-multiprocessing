import os
import shutil
from watchdog.events import FileSystemEventHandler
from pancard.pattern2 import PanCardPatteern2
from helpers.write_xml import WriteXML
from ocrr_logging.ocrr_engine_log import OCRREngineLogging

class PanCardPattern2Handler(FileSystemEventHandler):
    def on_created(self, event):
         # Configure logger
        config = OCRREngineLogging()
        logger = config.configure_logger()

        # Get the image path
        self.image_path = event.src_path

        # Get the image name
        image_file_name = os.path.basename(self.image_path)

         # Get the rejcted image path
        rejected_image_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\rejected_images'

        # Get the final redacted images folder path
        redacted_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\redacted_images'

        # Get xml file path
        xmls_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\redacted_images'

        # Collect pan card informations
        collect_pan_card_info_obj = PanCardPatteern2(self.image_path).collect_pan_card_info()

        if collect_pan_card_info_obj:
            WriteXML(xmls_path, image_file_name, collect_pan_card_info_obj ).writexml()
            logger.info(f"Writing XML file")

            # Move the image to finished folder
            shutil.move(self.image_path,  os.path.join(redacted_path, image_file_name))
            logger.info(f"Pan card moved to finished folder")         
        else:
            # Move the image to rejected folder
            shutil.move(self.image_path,  os.path.join(rejected_image_path, image_file_name))
            logger.error(f"Pan card {image_file_name} is rejected and moved to rejected folder") 