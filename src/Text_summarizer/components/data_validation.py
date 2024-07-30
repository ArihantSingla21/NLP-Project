import os 
from src.Text_summarizer.logging import logging 
from src.Text_summarizer.config.configuration import data_validation_config

class DataValidation:
    def __init__(self,config: data_validation_config):
        self.config=config
        
    def validate_all_files_exist(self)-> bool :
        try:
            validation_status = None 
            all_files = os.listdir(os.path.join("artifacts" , "data_ingestion", "samsum_dataset"))
            
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status= False
                    with open(self.config.STATUS_FILE,'w') as f :
                        f.write(f"validation status : {validation_status} for file {file}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f :
                        f.write(f"validation status : {validation_status} for file {file}")
            return validation_status            
        except Exception as e:
            raise e            
