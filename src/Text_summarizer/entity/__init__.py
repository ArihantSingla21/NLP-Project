from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class data_ingestionConfig:
    root_dir : Path
    source_URL :str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class data_validation_config:
    root_dir :Path
    STATUS_FILE : str
    ALL_REQUIRED_FILES : list    


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path : Path
    tokenizer_name : Path    