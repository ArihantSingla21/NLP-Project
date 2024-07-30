import os 
from src.Text_summarizer.config.configuration import ConfigurationManager
from src.Text_summarizer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):  
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        dv=DataValidation(config=data_validation_config)
        dv.validate_all_files_exist()
