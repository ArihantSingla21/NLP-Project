##loading all the important libraries 
import os 
from pathlib import Path
import zipfile
from src.Text_summarizer.logging import logging 
from src.Text_summarizer.utils.common import get_size
from urllib.request import Request,urlretrieve
from src.Text_summarizer.entity import data_ingestionConfig
from pathlib import Path    

class DataIngestion:
    def __init__(self,config : data_ingestionConfig):
        self.config=config
        
    def download_data(self):
        ## created the directory if it does not exist
        directory = os.path.dirname(self.config.local_data_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(self.config.local_data_file):
            filename,header = urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )    
            logging.info(f"{filename} downaloaded with following info : {header}")
        else:
            logging.info(f"file already exists of size : {get_size(Path(self.config.local_data_file))} ") 
            
    def extract_zip_file(self):
        unzip_path= self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)