from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path 

@dataclass
class DataValidationConfig:
    root_dir: Path
    local_data_file: Path
    STATUS_FILE: str 
    all_schema: dict 

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path