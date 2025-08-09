from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    ingested_train_file_path: str
    ingested_test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: dict
    test_metric_artifact: dict