import os, sys
import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from cyberSecurity.loggers import logger
from cyberSecurity.exceptions import CSException
from cyberSecurity.entity import DataTransformationConfig, DataTransformationArtifact
from cyberSecurity.constants import NUMERICAL_COLUMNS, CATEGORICAL_COLUMNS, TARGET_COLUMN 
from cyberSecurity.utils import save_bin

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def load_data(self) -> tuple:
        """Load Cyber Security Train and Test Datasets"""
        try:
            logger.info("Loading Datasets for Transformation")

            train_path = Path(self.config.data_path) / "train.csv"
            test_path = Path(self.config.data_path) / "test.csv"

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info(f"Train Data Shape: {train_df.shape}")
            logger.info(f"Test Data Shape: {test_df.shape}")

            return train_df, test_df
        except Exception as e:
            logger.error(f"Error Loading Data: {e}")
            raise CSException(e, sys)

    def get_data_transformer_object(self):
        try:
            numerical_columns = NUMERICAL_COLUMNS
            categorical_columns = CATEGORICAL_COLUMNS

            num_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ])

            logger.info(f"Categorical Columns: {categorical_columns}")
            logger.info(f"Numerical_columns: {numerical_columns}")

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipelines", cat_pipeline, categorical_columns)
            ])

            return preprocessor
        except Exception as e:
            raise CSException(e, sys)
    
    def initiate_date_tranformation(self) -> DataTransformationArtifact:
        try:
            logger.info(f"Data Transformation Started")

            train_df, test_df = self.load_data()

            logger.info(f"Obtaining Preprocessin Object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = TARGET_COLUMN

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis= 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis= 1)
            target_feature_test_df = test_df[target_column_name]

            logger.info(f"Applying Preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            logger.info("Saved Preprocessing Object.")

            save_bin(
                data=preprocessing_obj,
                path=self.config.preprocessor_obj_file_path
            )

            train_file_path = os.path.join(self.config.root_dir, "train.csv")
            test_file_path = os.path.join(self.config.root_dir, "test.csv")

            pd.DataFrame(train_arr).to_csv(train_file_path, index=False)
            pd.DataFrame(test_arr).to_csv(test_file_path, index=False)

            return DataTransformationArtifact(
                transformed_object_file_path=self.config.preprocessor_obj_file_path,
                transformed_train_file_path=train_file_path,
                transformed_test_file_path=test_file_path
            )
        except Exception as e:
            raise CSException(e, sys)