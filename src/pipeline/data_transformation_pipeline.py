from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logger import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.split_data()
            else:
                raise Exception("Your data scheme is not valid.")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n \n")
    except Exception as e:
        logger.exception(e) 
        raise e       


