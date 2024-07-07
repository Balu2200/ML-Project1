import logging
import os
from datetime import datetime

# Construct the log file name
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Create the log directory
log_path = os.path.join(os.getcwd(), "Logs")
os.makedirs(log_path, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



