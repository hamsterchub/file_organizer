# Import Python libs
import os
import shutil

# Wrapper around Logger setup to avoid circular import with app_logger.py
logger = None
def setup_util_functions_logger(logger_obj):
    global logger
    logger = logger_obj


# Print scoreboard to logs
# Inputs:
#       All integers
# Outputs:
#       None
def log_scoreboard(files, dirs, errors):
    logger.debug(f"\nSCOREBOARD:")
    logger.debug(f"Number of files processed = \"{files}\"")
    logger.debug(f"Number of directories processed = \"{dirs}\"")
    logger.debug(f"Number of errors seen = \"{errors}\"")
    return


# Tries to make a directory. Return False if there's an error
# Inputs:
#       str - Path to desired directory
# Outputs:
#       Bool - If creation failed
def os_make_dir(dir_path):
    try:
        os.makedirs(dir_path, exist_ok=True)

        # Avoids issues with linker due to circular imports with app_logger
        # Allows for the function to be valid before logger is setup
        if logger:
            logger.debug(f"Created directory: \"{dir_path}\"")
        else:
            print(f"Logger not setup yet. Only expected during linker execution")

    except OSError as e:
        logger.error(f"Couldn't create directory \"{dir_path}\": {e}")
        return False
    return True


# Move a file from one directory to another
# Inputs:
#       str - full path of file to move
#       str - destination directory
# Outputs:
#       None
def os_move_file(full_file_path, dest_dir):
    shutil.move(full_file_path, dest_dir)
    logger.info(f"Moved: \"{full_file_path}\" to \"{dest_dir}\"\n")
    return


# Inputs:
#       str - First thing to join
#       str - Second thing to join
# Outputs:
#       str - joined path
def os_join_path(join1, join2):
    return os.path.join(join1, join2)


# Return array of file/dir paths in a directory
# Inputs:
#       str - Directory path
# Outputs:
#       Array
def os_list_dir(dir_path):
    return os.listdir(dir_path)


# Returns True if the directory path exists
# Inputs:
#       str - File path
# Outputs:
#       Boolean
def os_does_dir_exist(dir_path):
    return os.path.exists(dir_path)


# Return extension of a file
# Inputs:
#       str - File path
# Outputs:
#       str - extension (ex: .jpg)
def os_get_file_ext(file_path):
    return os.path.splitext(file_path)[1].lower()


# Return True if file_path is a directory. Return False otherwise
# Inputs:
#       str - File/dir path
# Outputs:
#       Boolean
def os_is_path_a_dir(file_path):
    return not os.path.isfile(file_path)


# Return True if input_dir is an empty directory. Return False otherwise
# Inputs:
#       str - Directory path
# Outputs:
#       Boolean
def os_is_dir_empty(dir_path):
    if not os.listdir(dir_path):
        logger.debug(f"Directory is empty: \"{dir_path}\"")
        return True
    logger.debug(f"Directory is NOT empty: \"{dir_path}\"")
    return False


# Deletes input directory
# Inputs:
#       str - Path to an empty directory
# Outputs:
#       bool - True if directory was deleted successfully. False otherwise
def os_remove_empty_dir(dir_path):
    logger.debug(f"Directory is empty and needs to be cleaned up: \"{dir_path}\"")

    try:
        os.rmdir(dir_path)
        logger.info(f"Removed empty directory: \"{dir_path}\"")
    except OSError as e:
        logger.error(f"Error - Couldn't delete directory \"{dir_path}\": {e}")
        return False
    return True


# Check to see if a file with filename currently exists in full_output_path, and try to delete if so
# Inputs:
#       str - full output directory path
#       str - filename (not full path to file)
# Outputs:
#       bool - False if filename was found in full_output_path but did NOT successfully delete it. True otherwise
def deduplicate_output(full_output_path, filename):
    dest_file_path = os.path.join(full_output_path, filename)
    if os.path.exists(dest_file_path):
        logger.debug(f"This file already exists in the correct output directory: \"{dest_file_path}\"")
        try:
            os.remove(dest_file_path)
            logger.info(f"Action - Deleted duplicate of \"{dest_file_path}\"")
        except OSError as e:
            logger.error(f"Error - Couldn't delete the duplicate file \"{dest_file_path}\": {e}")
            return False
    return True