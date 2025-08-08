from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("config/params.yaml")

# Required columns for the dataset
REQUIRED_COLUMNS = [
    'creation_time', 'end_time', 'time', 'src_ip', 'dst_ip', 
    'src_ip_country_code', 'bytes_in', 'bytes_out', 'detection_types'
]

# Feature columns
FEATURE_COLUMNS = ['bytes_in', 'bytes_out', 'duration_seconds']
CATEGORICAL_COLUMNS = ['src_ip_country_code']
NUMERICAL_COLUMNS = ['bytes_in', 'bytes_out', 'duration_seconds']
TARGET_COLUMN = 'is_suspicious'

# Model artifacts
MODEL_FILE_NAME = "model.pkl"
PREPROCESSOR_FILE_NAME = "preprocessor.pkl"