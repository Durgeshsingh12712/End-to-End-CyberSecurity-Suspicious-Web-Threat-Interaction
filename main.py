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

try:
    logger.info(f">>>>>>> Data Tranformation Started <<<<<<<")
    training_pipeline = TrainingPipeline()
    training_pipeline.data_tranformation()
    logger.info(f">>>>>>> Data Tranformation Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>> Model Trainer Started <<<<<<<")
    training_pipeline = TrainingPipeline()
    training_pipeline.model_trainer()
    logger.info(f">>>>>>> Model Trainer Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>>> Model Evaluation Started <<<<<<<")
    training_pipeline = TrainingPipeline()
    training_pipeline.model_evaluation()
    logger.info(f">>>>>>> Model Evaluation Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e