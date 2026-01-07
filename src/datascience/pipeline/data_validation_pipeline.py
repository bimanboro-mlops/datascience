from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validataion import DataValidation

STAGE_NAME= "Data Validation Stage"
from src.datascience import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def Initiate_data_validation(self):
        logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        try:
            config= ConfigurationManager()
            data_validation_config= config.get_data_validation_config()

            data_validation= DataValidation(config= data_validation_config)

            data_validation.validate_all_columns()

            logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{'='*20} Data Ingestion Pipeline Started {'='*20}")
        obj= DataValidationTrainingPipeline()
        obj.Initiate_data_validation()
        logger.info(f"{'='*20} Data Validation Pipeline Completed {'='*20}")
    except Exception as e:
        logger.exception(e)
        raise e