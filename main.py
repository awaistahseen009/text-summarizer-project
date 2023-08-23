from src.text_summarizer.pipeline.stage_01_data_extraction import DataExtractionTrainingPipeline
from src.text_summarizer.logging import logger
try:
    logger.info(f"Stage Data Extraction started")
    data_extraction=DataExtractionTrainingPipeline()
    data_extraction.main()
    logger.info(f"Stage Data Extraction ended")
except Exception as e:
    logger.exception(e)
    raise e