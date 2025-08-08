from cyberSecurity.loggers import logger
from cyberSecurity.pipeline import TrainingPipeline

try:
    logger.info(f">>>>>>> Data Ingestion Started <<<<<<<")
    training_pipeline = TrainingPipeline()
    training_pipeline.data_ingestion()
    logger.info(f">>>>>>> Data Ingestion Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>> Data Validation Started <<<<<<<")
    training_pipeline = TrainingPipeline()
    training_pipeline.data_validation()
    logger.info(f">>>>>>> Data Validation Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e