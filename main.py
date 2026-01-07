from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"{'='*20} {STAGE_NAME} Started {'='*20}")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.Initiate_data_ingestion()
    logger.info(f"{'='*20} {STAGE_NAME} Completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e
