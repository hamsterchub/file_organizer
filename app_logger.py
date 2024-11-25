# Import Python libs
import datetime
import logging

# Import project files
from util_functions import os_make_dir, os_join_path

# Set Logger instance
logger = logging.getLogger(__name__)


# Setup console log handler
# Inputs:
#       logging.Formatter - Log format defined in setup_all_log_handlers function
#       Boolean - See "setup_all_log_handlers()" inputs definition block
# Outputs:
#       None
def setup_console_handler(handler_formatter, debug_mode):
    # Setup console handler logging level. If input argument is:
    #    True - Log everything
    #    False - Only log WARNING and above
    console_log_level = logging.DEBUG if debug_mode else logging.INFO
    logger.info("Debug mode is %s", debug_mode)

    # Setup console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(handler_formatter)
    logger.addHandler(console_handler)

    return


# Setup file log handler
# Inputs:
#       logging.Formatter - Log format defined in setup_all_log_handlers function
# Outputs:
#       Boolean - False if the output directory for logging couldn't be created. True otherwise
def setup_file_handler(handler_formatter):
    log_directory = "program_logs"
    if not os_make_dir(log_directory):
        return False

    # Define log file name for file handler
    log_file_name_local = datetime.datetime.now().strftime("app_log_%Y%m%d_%H%M%S.log")
    log_file_name_with_dir = os_join_path(log_directory, log_file_name_local)
    logger.info("Log file name for this run: %s", log_file_name_with_dir)

    # Setup file handler (INFO and above)
    file_handler = logging.FileHandler(log_file_name_with_dir)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(handler_formatter)
    logger.addHandler(file_handler)

    return True


# Setup all log handlers
# Inputs:
#       Boolean - True if program was invoked with --debug option. False otherwise
# Outputs:
#       Logger object
def setup_logger(debug_mode = False):
    if not logger.hasHandlers():    # Only setup the logger once
        logger.setLevel(logging.DEBUG)
        handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        setup_console_handler(handler_formatter, debug_mode)    # Setup console logger
        setup_file_handler(handler_formatter)                   # Setup file logger
    return logger