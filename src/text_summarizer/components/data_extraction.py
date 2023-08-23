import urllib.request as request 
import zipfile
import os
from text_summarizer.logging import logger
from text_summarizer.utils.common import get_file_size
from pathlib import Path
from text_summarizer.entity import (DataExtractionConfig)

class DataExtraction:
    def __init__(self,config:DataExtractionConfig):
        self.config=config
    def download_file(self):
        if  not os.path.exists(self.config.local_data):
            filename,headers=request.urlretrieve(
                url=self.config.source,
                filename=self.config.local_data
            )
            logger.info(f"File {filename} downloading with headers {headers}")
        else:
            logger.info(f"File {filename} already exits with size {get_file_size(Path(self.config.local_data))} ")
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data,'r') as ref:
            ref.extractall(unzip_path)