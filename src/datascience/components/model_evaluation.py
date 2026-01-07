import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from urllib.parse import urlparse
import mlflow
import numpy as np
from pathlib import Path
from src.datascience.utils.common import save_json

import os
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/BimanAdmin/datascience.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="BimanAdmin"
os.environ["MLFLOW_TRACKING_PASSWORD"]="XYZ"

class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self, actual, pred):
        rmse=np.sqrt(mean_squared_error(actual, pred))
        mae=mean_absolute_error(actual, pred)
        r2_square=r2_score(actual, pred)
        return rmse, mae, r2_square
    
    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop(columns=[self.config.target_column],axis=1)
        test_y=test_data[self.config.target_column]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities=model.predict(test_x)
            rmse, mae, r2_square=self.evaluate_model(test_y, predicted_qualities)

            scores={
                "rmse":rmse,
                "mae":mae,
                "r2_square":r2_square
            }

            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            if tracking_url_type_store!="file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model,"model")




    
