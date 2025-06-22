import os
import pandas as pd
from src.logger import logger
from src.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def split_data(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Splitted Data into Train and Test sets.")
        logger.info(f"Train set shape: {train.shape}")
        logger.info(f"Test set shape: {test.shape}")

        

