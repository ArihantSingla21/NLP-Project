from src.Text_summarizer.constants import *
from src.Text_summarizer.utils.common import create_directories,read_yaml
from src.Text_summarizer.logging import logging 
from src.Text_summarizer.entity import data_ingestionConfig,data_validation_config


class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params= read_yaml(params_file_path) 
        
        create_directories([self.config.artifacts_root])
        logging.info("created directory named artifacts")
        
        
        
    def get_data_ingestion_config(self)-> data_ingestionConfig:
        ## this is where we read the yaml file , to get the file path saved in the yaml file 
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        logging.info("creating directory named root_dir")
        ## again reading the yaml file 
        data_ingestion_config=data_ingestionConfig(    
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir)
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> data_validation_config:
        config= self.config.data_validation
        
        create_directories([config.root_dir])
        
        data_validation_configuration = data_validation_config(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
        )    
        
        return data_validation_configuration
            
        
        