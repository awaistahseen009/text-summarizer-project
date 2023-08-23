from src.text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml,create_dirs
from text_summarizer.entity import (DataExtractionConfig,DataValidationConfig)
class ConfigurationManager:
    def __init__(
        self,
        config_path=CONFIG_FILE_PATH,
        param_path=PARAM_FILE_PATH
    ):
        self.config=read_yaml(config_path)
        self.params=read_yaml(param_path)
        create_dirs([self.config.artifacts_root])

    def get_data_extraction_config(self)->DataExtractionConfig:
        create_dirs([self.config.data_extraction.root_dir])
        data_extraction_config=DataExtractionConfig(
            root_dir=self.config.data_extraction.root_dir,
            source= self.config.data_extraction.source,
            local_data=self.config.data_extraction.local_data,
            unzip_dir=self.config.data_extraction.unzip_dir
        )
        return data_extraction_config

    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation 
        create_dirs([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_req_files=config.all_req_files
        )
        return data_validation_config

        