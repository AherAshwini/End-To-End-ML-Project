import logging
import os
from datetime import datetime

###Below code creates log folder and logfile.
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"  ##Creates timestamped logfile.
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)  ##Defines logs directory.
os.makedirs(logs_path,exist_ok=True)  ##Ensure logs directory exists.

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)  ##Full log file path.


###Logging configuration.
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] line: %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level = logging.INFO,
)




