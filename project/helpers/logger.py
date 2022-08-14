import os
import logging

class Logger:
    """
    Setea el logger propio de la librería logging y wrappea sus métodos
    """
    LOG_FOLDER = "logs"
    LOG_FILE_NAME = "app.log"
    LOG_FILE_PATH = f"{LOG_FOLDER}/{LOG_FILE_NAME}"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(self):
        self.create_log_folder_if_not_exists()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(Logger.LOG_FORMAT)
        file_handler = logging.FileHandler(Logger.LOG_FILE_PATH)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def create_log_folder_if_not_exists(self):
        if not os.path.exists(Logger.LOG_FOLDER):
            os.makedirs(Logger.LOG_FOLDER)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
