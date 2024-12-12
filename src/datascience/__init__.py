import os
import sys
import logging

# Logging is a crucial tool in programming for tracking the execution of code, diagnosing issues, and maintaining
#  applicationsLogging is a crucial tool in programming for tracking the execution of code, diagnosing issues,
#  and maintaining applications

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("datasciencelogger")