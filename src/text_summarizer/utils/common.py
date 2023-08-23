import os
import box
from box.exceptions import BoxValueError
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path:Path)->ConfigBox:
    try:
        with open(path,'r') as yaml_file:
            doc=yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded {path} ,yaml file")
            return ConfigBox(doc)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
@ensure_annotations
def create_dirs(paths:list,verbose=False):
    for path in paths:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"{path} created successfully !")

@ensure_annotations
def get_file_size(path:Path):
    return f"{round(os.path.getsize(path)/1024)} KB"