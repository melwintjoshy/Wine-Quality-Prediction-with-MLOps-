from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logger import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config = model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            logger.exception(e) 
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n \n")
    except Exception as e:
        logger.exception(e) 
        raise e       

