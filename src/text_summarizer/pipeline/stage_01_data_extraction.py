from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_extraction import DataExtraction
from text_summarizer.logging import logger

class DataExtractionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_extraction_config=config.get_data_extraction_config()
        data_extraction=DataExtraction(config=data_extraction_config)
        data_extraction.download_file()
        data_extraction.extract_zip_file()