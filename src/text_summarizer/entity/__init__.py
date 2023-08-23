from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataExtractionConfig:
    root_dir:Path
    source: str
    local_data: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    status_file:str
    all_req_files:list
