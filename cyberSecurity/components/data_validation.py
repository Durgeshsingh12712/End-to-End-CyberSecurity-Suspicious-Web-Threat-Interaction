import sys
import pandas as pd
from cyberSecurity.loggers import logger
from cyberSecurity.exceptions import CSException
from cyberSecurity.entity import DataValidationConfig, DataValidationArtifact
from cyberSecurity.constants import REQUIRED_COLUMNS

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = REQUIRED_COLUMNS

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            
            return validation_status
        except Exception as e:
            raise CSException(e, sys)
    
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            logger.info(f"Data Validation Started")
            validation_status = self.validate_all_columns()

            if validation_status:
                message = "Data Validation Passed Successfully"
                logger.info(message)
            else:
                message = "Data Validation Failed - Schema Mismatch"
                logger.error(message)
            
            return DataValidationArtifact(
                validation_status=validation_status,
                message = "Data Validation Completed"
            )
        except Exception as e:
            raise CSException(e, sys)