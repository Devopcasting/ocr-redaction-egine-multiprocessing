from pancard.main import PanCardInfo

class PanCardPatteern1:
    def __init__(self, image_path) -> None:
        self.image_path = image_path
    
    def collect_pan_card_info(self) -> list:
        pan_card_info_obj = PanCardInfo(self.image_path)
        pan_card_info_list = []

        # Check : pan card number
        pan_card_number = pan_card_info_obj.extract_pan_card_number()
        if not pan_card_number or len(pan_card_number) == 0:
            return False
        else:
            pan_card_info_list.append(pan_card_number)

        # Check: pan card dob
        pan_card_dob = pan_card_info_obj.extract_dob()
        if not pan_card_dob or len(pan_card_dob) == 0:
            return False
        else:
            pan_card_info_list.append(pan_card_dob)
        
        return pan_card_info_list
    