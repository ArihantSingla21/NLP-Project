from src.Text_summarizer.pipeline.stage_01_data_inegstion import DataIngestionTrainingPipeline
from src.Text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.Text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Text_summarizer.logging import logging 

    
STAGE_NAME= "data ingestion"

try:
    logging.info(f"//// stage {STAGE_NAME} ")    
    data_inegstion= DataIngestionTrainingPipeline()
    data_inegstion.main()
    logging.info(f"{STAGE_NAME} has been completed")
except Exception as e:
    logging.exception(e)
    raise e    



STAGE_NAME= "data validation"

try:
    logging.info(f"//// stage {STAGE_NAME} ")    
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f"{STAGE_NAME} has been completed")
except Exception as e:
    logging.exception(e)
    raise e    


STAGE_NAME= "data transformation"

try:
    logging.info(f"//// stage {STAGE_NAME} ")    
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.main()
    logging.info(f"{STAGE_NAME} has been completed")
except Exception as e:
    logging.exception(e)
    raise e    


