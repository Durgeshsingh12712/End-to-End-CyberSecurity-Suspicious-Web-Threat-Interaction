from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    ingested_train_file_path: str
    ingested_test_file_path: str