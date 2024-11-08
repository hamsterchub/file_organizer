import os
import shutil

# Print scoreboard
# Inputs:
#       All integers
# Outputs:
#       None
def print_scoreboard(files, dirs, errors):
    print(f"\nSCOREBOARD:")
    print(f"Number of files processed = \"{files}\"")
    print(f"Number of directories processed = \"{dirs}\"")
    print(f"Number of errors seen = \"{errors}\"")
    return


# Tries to make a directory. Return False if there's an error
# Inputs:
#       str - Path to desired directory
# Outputs:
#
def os_make_dir(dir_path):
    try:
        os.makedirs(dir_path)
        print(f"Action - Created new directory: \"{dir_path}\"")
    except OSError as e:
        print(f"Error - Couldn't create directory \"{dir_path}\": {e}")
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
    print(f"Action - Moved: \"{full_file_path}\" to \"{dest_dir}\"\n")
    return


# Return full path of a directory and a file within it
# Inputs:
#       str - Directory path
#       str - "local" file name
# Outputs:
#       str - joined path (ex. C:/Users/Bob/Input/image.jpg)
def os_join_pathy(dir_path, file_name):
    return os.path.join(dir_path, file_name)


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
        print(f"Log - \"{dir_path}\" is empty")
        return True
    print(f"Log - \"{dir_path}\" is NOT empty")
    return False


# Deletes input directory
# Inputs:
#       str - Path to an empty directory
# Outputs:
#       bool - True if directory was deleted successfully. False otherwise
def os_remove_empty_dir(dir_path):
    print(f"Log - \"{dir_path}\" is an empty folder that needs to be cleaned up. Attempting to delete folder...")

    try:
        os.rmdir(dir_path)
        print(f"Action - Removed empty directory: \"{dir_path}\"")
    except OSError as e:
        print(f"Error - Couldn't delete directory \"{dir_path}\": {e}")
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
        print(f"Log - This file already exists in the correct output directory. Attempting to delete the duplicate...")
        try:
            os.remove(dest_file_path)
            print(f"Action - Deleted duplicate of \"{dest_file_path}\"")
        except OSError as e:
            print(f"Error - Couldn't delete the duplicate file \"{dest_file_path}\": {e}")
            return False
    return True


# Create desired output directory if it doesn't exist yet
# Inputs:
#       str - Output directory from __main__ invocation
#       str - Derived output directory from handler function
# Outputs:
#       0 - Error with creating desired output directory
#       str - Full output directory
def os_create_output_dir(output_dir, partial_output_path):
    # Set full output path
    full_output_path = os.path.join(output_dir, partial_output_path)
    print(f"Log - Output directory is \"{full_output_path}\"")
    
    # Create the full output path subdirectory if it doesn't exist
    if not os.path.exists(full_output_path):
        print(f"Log - Directory \"{full_output_path}\" doesn't exist. Attempt to create this directory...")
        try:
            os.makedirs(full_output_path)
            print(f"Action - Created directory \"{full_output_path}\"")
        except OSError as e:
            print(f"Error - Couldn't create the new directory \"{full_output_path}\": {e}")
            return 0
    return full_output_path