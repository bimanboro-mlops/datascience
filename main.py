from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"{'='*20} {STAGE_NAME} Started {'='*20}")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.Initiate_data_ingestion()
    logger.info(f"{'='*20} {STAGE_NAME} Completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation Stage"

try:
    logger.info(f"{'='*20} {STAGE_NAME} Started {'='*20}")
    data_validation= DataValidationTrainingPipeline()
    data_validation.Initiate_data_validation()
    logger.info(f"{'='*20} {STAGE_NAME} Completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Transformation Stage"

try:
    logger.info(f"{'='*20} {STAGE_NAME} Started {'='*20}")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.Initiate_data_transformation()
    logger.info(f"{'='*20} {STAGE_NAME} Completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Model Training Stage"

try:
    logger.info(f"{'='*20} {STAGE_NAME} Started {'='*20}")
    model_trainer= ModelTrainerPipeline()
    model_trainer.Initiate_model_training()
    logger.info(f"{'='*20} {STAGE_NAME} Completed {'='*20}")
except Exception as e:
    logger.exception(e)
    raise e
