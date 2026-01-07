from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger



STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def Initiate_model_evaluation(self):
        logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        try:
            config= ConfigurationManager()
            model_evaluation_config= config.get_model_evaluation_config()

            model_evaluation= ModelEvaluation(config= model_evaluation_config)

            model_evaluation.log_into_mlflow()

            logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{'='*20} Model Evaluation Pipeline Started {'='*20}")
        obj= ModelEvaluationPipeline()
        obj.Initiate_model_evaluation()
        logger.info(f"{'='*20} Model Evaluation Pipeline Completed {'='*20}")
    except Exception as e:
        logger.exception(e)
        raise e