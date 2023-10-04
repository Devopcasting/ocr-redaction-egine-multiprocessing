import logging


class OCRREngineLogging:
    def __init__(self, log_file_path=r'C:\Users\pokhriyal\Desktop\Project-OCRR\logs\ocrr_engine.log', log_level=logging.DEBUG):
        self.log_file_path = log_file_path
        self.log_level = log_level

        # Create a logger object
        self.logger = logging.getLogger()

        # Set the log level
        self.logger.setLevel(log_level)

        # Create a file handler
        file_handler = logging.FileHandler(log_file_path)

        # Create a formatter
        formatter = logging.Formatter('%(process)d %(asctime)s %(levelname)s %(message)s')

        # Add the formatter to the file handler
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def log(self, msg, level=logging.INFO):
        self.logger.log(level, msg)

    def debug(self, msg):
        self.log(msg, logging.DEBUG)

    def info(self, msg):
        self.log(msg, logging.INFO)

    def warning(self, msg):
        self.log(msg, logging.WARNING)

    def error(self, msg):
        self.log(msg, logging.ERROR)

    def critical(self, msg):
        self.log(msg, logging.CRITICAL)
