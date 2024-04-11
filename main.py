from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException

import sys
import os

from cellSegmentation.pipeline.training_pipeline import TrainPipeline


# Testing

# STAGE_NAME = "Data ingestion stage"
# try:
#     logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = TrainPipeline()
#     data_ingestion_art = obj.start_data_ingestion()
#     logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     raise AppException(e,sys)



# STAGE_NAME = "Data Validation stage"

# try:
#     logging.info(f">>>>>> stage {STAGE_NAME} started<<<<<<")
#     data_validation = TrainPipeline()

#     data_validation.start_data_validation(data_ingestion_art)
#     logging.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==============x")

# except Exception as e:
#     logging.exception(e)
#     raise AppException(e,sys)



# STAGE_NAME = "Model trainer stage"

# try:
#     logging.info(f">>>>>> stage {STAGE_NAME} started<<<<<<")
#     model_trainer = ModelTrainerTrainingPipeline()
#     model_trainer.main()
#     logging.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==============x")

# except Exception as e:
#     raise AppException(e,sys)

if __name__ =="__main__":

    obj = TrainPipeline()
    obj.run_pipeline()