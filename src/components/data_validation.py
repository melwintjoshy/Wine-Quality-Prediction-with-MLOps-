import os 
import urllib.request
import pandas as pd
from src.logger import logger
from src.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.local_data_file)
            data_schema = {col: str(dtype) for col, dtype in data.dtypes.items()}

            expected_schema = dict(self.config.all_schema)

            validation_status = data_schema == expected_schema

            # Log and write validation result
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            if validation_status:
                logger.info("Validation Successful.")
            else:
                logger.warning("Validation Failed.")

            return validation_status
        except Exception as e:
            raise e