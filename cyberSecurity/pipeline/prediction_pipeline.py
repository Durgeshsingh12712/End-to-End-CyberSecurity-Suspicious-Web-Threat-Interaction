import sys
import pandas  as pd
from pathlib import Path

from cyberSecurity.loggers import logger
from cyberSecurity.exceptions import CSException
from cyberSecurity.utils import load_bin

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = "artifacts/model_trainer/model.pkl"
            preprocessor_path = "artifacts/data_transformation/preprocessor.pkl"

            print("Before Loading")
            model = load_bin(Path(model_path))
            preprocessor = load_bin(Path(preprocessor_path))
            print("After Loading")

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds
        except Exception as e:
            raise CSException(e, sys)
    
class CustomData:
    def __init__(self,
                 bytes_in: float,
                 bytes_out: float,
                 duration_seconds: float,
                 src_ip_country_code: str):
        self.bytes_in = bytes_in
        self.bytes_out = bytes_out
        self.duration_seconds = duration_seconds
        self.src_ip_country_code = src_ip_country_code
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "bytes_in": [self.bytes_in],
                "bytes_out": [self.bytes_out],
                "duration_seconds": [self.duration_seconds],
                "src_ip_country_code": [self.src_ip_country_code]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CSException(e, sys)
        