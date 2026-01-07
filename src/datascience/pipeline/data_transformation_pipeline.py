from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger

STAGE_NAME= "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def Initiate_data_transformation(self):
        logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        try:
            config= ConfigurationManager()
            data_transformation_config= config.get_data_transformation_config()

            data_transformation= DataTransformation(config= data_transformation_config)

            data_transformation.train_test_split()

            logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{'='*20} Data Ingestion Pipeline Started {'='*20}")
        obj= DataTransformationTrainingPipeline()
        obj.Initiate_data_transformation()
        logger.info(f"{'='*20} Data Transformation Pipeline Completed {'='*20}")
    except Exception as e:
        logger.exception(e)
        raise e