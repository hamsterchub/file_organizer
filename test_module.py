# Import project files
import util_functions

# Logger
#    One-time setup of logger in util_functions to avoid circular imports
from app_logger import setup_logger
logger = setup_logger(True)
util_functions.setup_util_functions_logger(logger)


# Function to be called upon program invocation
if __name__ == "__main__":
    # Set input and output directories
    input_dir_main = "E:\Development\Python\File Organizer\Input"
    logger.info(f"Input directory: \"{input_dir_main}\"")
    output_dir_main = "E:\Development\Python\File Organizer\Output"
    logger.info(f"Output directory: \"{output_dir_main}\"")

    logger.debug(f"Log - Entering main\n")