from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE_NAME= "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def Initiate_data_ingestion(self):
        logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        try:
            config= ConfigurationManager()
            data_ingestion_config= config.get_data_ingestion_config()

            data_ingestion= DataIngestion(config= data_ingestion_config)

            data_ingestion.download_file()

            data_ingestion.extract_zip_file()

            logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{'='*20} Data Ingestion Pipeline Started {'='*20}")
        obj= DataIngestionTrainingPipeline()
        obj.Initiate_data_ingestion()
        logger.info(f"{'='*20} Data Ingestion Pipeline Completed {'='*20}")
    except Exception as e:
        logger.exception(e)
        raise e