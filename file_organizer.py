# Import project files
import util_functions
from handler_functions import get_file_type_handler

# Logger
#    One-time setup of logger in util_functions to avoid circular imports
from app_logger import setup_logger
logger = setup_logger()
util_functions.setup_util_functions_logger(logger)


# Main program logic
# Inputs:
#       str - Directory to parse for files. May either be the directory defined in the __main__ function or a nested folder, parsed recursively
#       str - Parent directory to move files to. Most if not all files will be moved into a subdirectory under here
#           Only defined in __main__. Not meant to be redefined by recursive calls
#       bool - Indicate if the function is running recursively. Set to True explicitly by recursive call inside this function
#           This is used to avoid deleting the source input directory defined in __main__ since the program will attempt to delete input_dir if it's empty
#       int - Running count of files processed. Need this due to the recursion. NOT mission-critical functionality
#       int - Running count of directories processed. Need this due to the recursion. NOT mission-critical functionality
#       int - Running count of errors encountered. Need this due to the recursion. NOT mission-critical functionality
# Outputs:
#       [int, int, int] - To be used by scoreboard printer functionality or append after recursive run. NOT mission-critical functionality
def run_main(input_dir, output_dir, is_recursive = False, num_files_processed = 0, num_folders_removed = 0, num_errors = 0):
    
    # Check if the input directory doesn't exist
    if not util_functions.os_does_dir_exist(input_dir):
        logger.critical(f"The input directory doesn't exist! Exiting main. Directory: \"{input_dir}\"")
        return [num_files_processed, num_folders_removed, num_errors]

    # Loop through all files in the input directory
    for filename in util_functions.os_list_dir(input_dir):
        file_path = util_functions.os_join_path(input_dir, filename)
        logger.info(f"Current file path being analyzed: \"{file_path}\"")

        # Templatized log output for any errors while processing this file
        warning_logger_output = f"Error caught. Will not process this file: \"{file_path}\""
              
        # Get the correct handler function for the extension of the current path (or 0 if current path is a folder)
        file_type_handler = get_file_type_handler(file_path)

        # Check if file_path is a directory (return code 0 from get_file_type_handler function). If so, recursively call run_main
        # Since the function is recursive, need to add the running counts from nested runs to the current run
        if file_type_handler == 0:
            recursive_run_main_return = run_main(file_path, output_dir, True, num_files_processed, num_folders_removed, num_errors)
            num_files_processed += recursive_run_main_return[0]
            num_folders_removed += recursive_run_main_return[1]
            num_errors += recursive_run_main_return[2]
            continue
        
        # Get the "local" output path to be appended to output_dir, and handle error if needed
        local_output_path = file_type_handler(file_path)
        if not local_output_path:   # There was an issue opening an image file
            logger.warning(warning_logger_output)
            num_errors += 1
            continue
        
        # Get full output directory and create if it doesn't exist
        full_output_path = util_functions.os_join_path(output_dir, local_output_path)
        if not util_functions.os_make_dir(full_output_path):    # There was an error in creating the output directory
            logger.warning(warning_logger_output)
            num_errors += 1
            continue

        # Check to see if the current file already exists in the appropriate destination folder and attempt to delete it
        bool_find_dupes_out = util_functions.deduplicate_output(full_output_path, filename)
        if not bool_find_dupes_out: # File was not successfully deleted
            logger.warning(warning_logger_output)
            num_errors += 1
            continue
        
        # Move the file to the full output path subdirectory and increment successful procs by 1
        util_functions.os_move_file(file_path, full_output_path)
        num_files_processed += 1

    # Checks for empty input directory. Delete the input_dir unless is_recursive is set to FALSE
    if util_functions.os_is_dir_empty(input_dir):
        if is_recursive:
            bool_cleanup_output = util_functions.os_remove_empty_dir(input_dir) # False if cleanup had an error, True otherwise

            # Increment correct stat based on cleanup function return value
            if bool_cleanup_output:
                num_folders_removed += 1
            else:
                num_errors += 1

            logger.info(f"The nested input directory is empty: \"{input_dir}\"")
            return [num_files_processed, num_folders_removed, num_errors]

        # This will be executed if input_dir is empty and is_recursive is FALSE
        logger.info(f"The program input directory is empty: \"{input_dir}\"")
        return [num_files_processed, num_folders_removed, num_errors]

    # If there's issues processing 1+ files in a directory, you'll hit this
    logger.info(f"There's at least 1 file still in \"{input_dir}\"")
    logger.info(f"User needs to manually investigate remaining file(s) in \"{input_dir}\"")
    return [num_files_processed, num_folders_removed, num_errors]


# Function to be called upon program invocation
if __name__ == "__main__":
    # Set input and output directories
    input_dir_main = "E:\Development\Python\File Organizer\Input"
    logger.info(f"Input directory: \"{input_dir_main}\"")
    output_dir_main = "E:\Development\Python\File Organizer\Output"
    logger.info(f"Output directory: \"{output_dir_main}\"")

    logger.debug(f"Log - Entering main\n")
    main_out = run_main(input_dir_main, output_dir_main)
    logger.info(f"Program complete!")
    util_functions.log_scoreboard(main_out[0], main_out[1], main_out[2])