import logging
from logging.handlers import RotatingFileHandler
import os

# Create log directory
os.makedirs("logs", exist_ok=True)


# File path
LOG_FILE = "logs/app.log"


# Create logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# File handler (rotating log)
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3
)

# Console handler
console_handler = logging.StreamHandler()

# Format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# # Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
