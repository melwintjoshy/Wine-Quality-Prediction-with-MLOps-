import os
import pandas as pd
import numpy as np
from src.utils.main_utils import save_json
from src.logger import logger
from src.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
from pathlib import Path
import mlflow
import mlflow.sklearn
import joblib
import dagshub

dagshub.init(repo_owner='melwintjoshy', repo_name='Mlops-proj1', mlflow=True)

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, y_test, y_pred):
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        X_test  = test_data.drop(self.config.target_column, axis = 1)
        y_test = test_data[[self.config.target_column]]

        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        
        with mlflow.start_run():
            y_pred = model.predict(X_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path = Path(self.config.metric_file_name), data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            
            mlflow.log_artifact(self.config.model_path, artifact_path="ElasticNet_Model")
            


