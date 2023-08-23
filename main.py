from src.text_summarizer.pipeline.stage_01_data_extraction import DataExtractionTrainingPipeline
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

from src.text_summarizer.logging import logger
try:
    logger.info(f"Stage Data Extraction started")
    data_extraction=DataExtractionTrainingPipeline()
    data_extraction.main()
    logger.info(f"Stage Data Extraction ended")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f"Stage Data Validation started")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Stage Data Validation ended")
except Exception as e:
    logger.exception(e)
    raise e