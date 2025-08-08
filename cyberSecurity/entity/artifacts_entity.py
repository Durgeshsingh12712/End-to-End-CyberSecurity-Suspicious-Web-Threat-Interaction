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