from src.text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml,create_dirs
from text_summarizer.entity import (DataExtractionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig)
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

    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation
        create_dirs([config.root_dir])
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer=config.tokenizer
        )
        return data_transformation_config

    def get_model_trainer_config(self)->ModelTrainerConfig:
        config=self.config.model_trainer
        params=self.params.TrainingArguments
        create_dirs([config.root_dir])
        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            per_device_eval_batch_size= params.per_device_eval_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )
        return model_trainer_config

        