import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Identify project root (2 levels above this file)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
LOG_DIR = os.path.join(project_root, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Use date only (not time) so all runs on same day use same file
LOG_FILE = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Flag to ensure we only configure once
_configured = False

def get_logger(name="mlops_logger"):
    """Get or create a logger with file and console handlers"""
    global _configured
    
    logger = logging.getLogger(name)
    
    # Only configure once
    if not _configured:
        logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s")
        
        # File handler - logs DEBUG and above to file
        file_handler = RotatingFileHandler(
            LOG_FILE_PATH,
            maxBytes=5 * 1024 * 1024,  # 5MB
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler - logs INFO and above to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        _configured = True
    
    return logger

# Create default logger instance
logger = get_logger()