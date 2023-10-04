from pancard.main import PanCardInfo
from ocrr_logging.ocrr_engine_log import OCRREngineLogging

class PanCardPatteern1:
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        # Configure logger
        self.logger = OCRREngineLogging()

    def collect_pan_card_info(self) -> list:
        pan_card_info_obj = PanCardInfo(self.image_path)
        pan_card_info_list = []

        # Check : pan card number
        pan_card_number = pan_card_info_obj.extract_pan_card_number()
        if not pan_card_number or len(pan_card_number) == 0:
            self.logger.error("PANERR002")
            return False
        else:
            pan_card_info_list.append(pan_card_number)

        # Check: pan card dob
        pan_card_dob = pan_card_info_obj.extract_dob()
        if not pan_card_dob or len(pan_card_dob) == 0:
            self.logger.error("PANERR003") 
            return False
        else:
            pan_card_info_list.append(pan_card_dob)
        
        return pan_card_info_list
    