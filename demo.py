# below code is to check the logging config
# from src.logger import logger

# logger.debug("Debug message test")
# logger.info("Info message test")
# logger.error("Error message test")


# --------------------------------------------------------------------------------

# # below code is to check the exception config
# from src.logger import logger
# from src.exception import MyException
# import sys

# try:
#     a = 1 + 'Z'
# except Exception as e:
#     logger.info(f"An exception occurred: {e}")
#     raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()