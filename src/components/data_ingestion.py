import os 
import urllib.request
from src.logger import logger
from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file (self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urllib.request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded.")
        else:
            logger.info("File already exists.")