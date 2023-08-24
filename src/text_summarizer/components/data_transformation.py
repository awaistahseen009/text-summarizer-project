from text_summarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from text_summarizer.entity import DataTransformationConfig
import os
class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizer)
    def convert_examples_to_features(self,examples):
        input_encoding=self.tokenizer(examples['dialogue'],max_length=1024,truncation=True)
        with self.tokenizer.as_target_tokenizer():
            target_encoding=self.tokenizer(examples['summary'],max_length=128,truncation=True)
        return {
            'input_ids':input_encoding['input_ids'],
            'attention_mask':input_encoding['attention_mask'],
            'labels':target_encoding['input_ids']
        }
    def convert(self):
        samsum_dataset=load_from_disk(self.config.data_path)
        samsum_dataset_trans=samsum_dataset.map(self.convert_examples_to_features,batched=True)
        samsum_dataset_trans.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))