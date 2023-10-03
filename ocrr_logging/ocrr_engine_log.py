import logging


class OCRREngineLogging:
    def __init__(self, log_file='C:\\Users\\pokhriyal\\Desktop\\Project-OCRR\\logs\ocrr_engine.log', log_level=logging.INFO) -> None:
        self.log_file = log_file
        self.log_level = log_level
    
    def configure_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger
    