import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok= True)

logging.basicConfig(
    level = logging.DEBUG,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath), #file handler is used to write logs to the filepath
        logging.StreamHandler(sys.stdout) #stream handler is used to display logs in the console
    ]   
)

logger = logging.getLogger()