from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataExtractionConfig:
    root_dir:Path
    source: str
    local_data: Path
    unzip_dir: Path