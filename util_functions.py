import os


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


# Return True if input_dir is an empty directory. Return False otherwise
# Inputs:
#       str - Directory path
# Outputs:
#       Boolean
def is_dir_empty(dir_path):
    if not os.listdir(dir_path):
        print(f"Log - \"{dir_path}\" is empty")
        return True
    print(f"Log - \"{dir_path}\" is NOT empty")
    return False


# Inputs:
#       str - Path to an empty directory
# Outputs:
#       bool - True if directory was deleted successfully. False otherwise
def remove_empty_dir(dir_path):
    print(f"Log - \"{dir_path}\" is an empty folder that needs to be cleaned up. Attempting to delete folder...")

    try:
        os.rmdir(dir_path)
        print(f"Action - Removed empty directory: \"{dir_path}\"")
    except OSError as e:
        print(f"Error - Couldn't delete directory \"{dir_path}\": {e}")
        return False
    return True


# Check to see if a file with filename currently exists in full_output_path
# Inputs:
#       str - full output directory path
#       str - filename (not full path to file)
# Outputs:
#       bool - False if filename was found in full_output_path but did NOT successfuolly delete it. True otherwise
def find_dupes(full_output_path, filename):
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
def create_output_dir(output_dir, partial_output_path):
    # Set full output path
    full_output_path = os.path.join(output_dir, partial_output_path)
    print(f"Log - Output directory is \"{full_output_path}\"")
    
    # Create the full output path subdirectory if it doesn't exist
    if not os.path.exists(full_output_path):
        print(f"Log - Directory \"{full_output_path}\" doesn't exist. Attempt to create this directory...")
        try:
            os.makedirs(full_output_path)
            print(f"Action - Directory \"{full_output_path}\" created")
        except OSError as e:
            print(f"Error - Couldn't create the new directory \"{full_output_path}\": {e}")
            return 0
    return full_output_path