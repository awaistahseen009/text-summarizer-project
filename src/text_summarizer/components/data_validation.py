import os
from text_summarizer.logging import logger
from text_summarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config 
    def validate_existance(self)->bool:
        try:
            validation_status=None
            all_files=os.listdir(os.path.join("artifacts","data_extraction","samsum_dataset"))
            for file in all_files:
                if file not in self.config.all_req_files:
                    validation_status=False
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation status : {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation status : {validation_status}")
            return validation_status
        except Exception as e:
            raise e  

