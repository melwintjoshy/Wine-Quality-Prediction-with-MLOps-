import os
import pandas as pd
from src.logger import logger
from src.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def training(self):
        train_data = pd.read_csv(self.config.train_data_path)

        X_train = train_data.drop(self.config.target_column, axis = 1)
        y_train = train_data[[self.config.target_column]]

        lr = ElasticNet(alpha = self.config.alpha, l1_ratio=self.config.l1_ratio, random_state= 42)
        lr.fit(X_train, y_train)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
    