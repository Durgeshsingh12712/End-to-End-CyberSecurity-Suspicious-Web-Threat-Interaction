import os, sys
import pandas as pd
import urllib.request as request
from pathlib import Path

from sklearn.model_selection import train_test_split

from cyberSecurity.loggers import logger
from cyberSecurity.exceptions import CSException
from cyberSecurity.entity import DataIngestionConfig, DataIngestionArtifact
from cyberSecurity.utils import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
            else:
                logger.info(f"File Already Exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            raise CSException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info(f"Data Ingestion Started")

            self.download_file()
            logger.info(f"Successfully Download Data")

            df = pd.read_csv(self.config.local_data_file)
            logger.info(f"Dataset Shape: {df.shape}")

            df = df.dropna().reset_index(drop=True)
            logger.info(f"After Drop None Values : {df.shape}")

            df = df.drop_duplicates().reset_index(drop=True)
            logger.info(f"After remove duplicates : {df.shape}")

            df['creation_time'] = pd.to_datetime(df['creation_time'])
            df['end_time'] = pd.to_datetime(df['end_time'])
            df['time'] = pd.to_datetime(df['time'])
            df['src_ip_country_code'] = df['src_ip_country_code'].str.upper()
            df['duration_seconds'] = (df['end_time'] - df['creation_time']).dt.total_seconds()
            df['is_suspicious'] = (df['detection_types'] == 'waf_rule').astype(int)

            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            train_file_path = os.path.join(self.config.root_dir, "train.csv")
            test_file_path = os.path.join(self.config.root_dir, "test.csv")

            train_set.to_csv(train_file_path, index = False, header =True)
            test_set.to_csv(test_file_path, index = False, header = True)

            logger.info("Data Ingestion Completed")

            return DataIngestionArtifact(
                ingested_train_file_path=train_file_path,
                ingested_test_file_path=test_file_path
            )
        except Exception as e:
            raise CSException(e, sys)