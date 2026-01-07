from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger

STAGE_NAME= "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def Initiate_model_training(self):
        logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        try:
            config= ConfigurationManager()
            model_trainer_config= config.get_model_transformation_config()

            model_trainer= ModelTrainer(config= model_trainer_config)

            model_trainer.train_model()

            logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{'='*20} Model Training Pipeline Started {'='*20}")
        obj= ModelTrainerPipeline()
        obj.Initiate_model_training()
        logger.info(f"{'='*20} Model Training Pipeline Completed {'='*20}")
    except Exception as e:
        logger.exception(e)
        raise e