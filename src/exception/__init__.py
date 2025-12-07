import sys
from src.logger import logger

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.
    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Create a formatted error message string
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    return error_message


class MyException(Exception):
    """
    Custom exception class for handling errors with detailed logging.
    """
    def __init__(self, error_message: Exception, error_detail: sys):
        """
        Initializes MyException with a detailed error message.
        :param error_message: The original exception.
        :param error_detail: The sys module to access traceback details.
        """
        # Call the base class constructor
        super().__init__(str(error_message))
        
        # Format the detailed error message
        self.error_message = error_message_detail(error_message, error_detail)
        
        # Log the error using the configured logger
        logger.error(self.error_message)
    
    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message