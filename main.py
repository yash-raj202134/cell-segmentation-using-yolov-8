from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException

import sys
import os

from cellSegmentation.pipeline.training_pipeline import TrainPipeline




STAGE_NAME = "Data ingestion stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = TrainPipeline()
    obj.start_data_ingestion()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise AppException(e,sys)