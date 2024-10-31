import os

# Import project files
from image_handler import get_image_output_path


# Inputs:
#       str - Full path to a file
#       NOTE - Currently unused...
# Outputs:
#       Desired subdirectory in the program output directory (defined in __main__) to drop files with an unsupported (by this program) file extension
def get_other_output_path(other_path):
    return "other"


# Inputs:
#       str - Full path to a file
#           NOTE - Currently unused...
# Outputs:
#       Desired subdirectory in the program output directory (defined in __main__) to drop files with a video type file extension
def get_video_output_path(video_path):
    return "videos"


# Inputs:
#       str - Full path to a file
#           NOTE - Currently unused...
# Outputs:
#       Desired subdirectory in the program output directory (defined in __main__) to drop files with a video type file extension
def get_word_output_path(word_path):
    return "word_docs"


# Inputs:
#       str - Full path to a file
#           NOTE - Currently unused...
# Outputs:
#       Desired subdirectory in the program output directory (defined in __main__) to drop files with a pdf type file extension
def get_pdf_output_path(pdf_path):
    return "pdf"


# Inputs:
#       str - Full path to a file
#           NOTE - Currently unused...
# Outputs:
#       Desired subdirectory in the program output directory (defined in __main__) to drop files with a powerpoint type file extension
def get_ppt_output_path(ppt_path):
    return "powerpoints"


# Inputs:
#       str - Full path to a file
#           NOTE - Currently unused...
# Outputs:
#       Desired subdirectory in the program output directory (defined in __main__) to drop files with a spreadsheet type file extension
def get_excel_output_path(excel_path):
    return "excel"


# Returns the correct file type handler function based on the file extension
# Inputs:
#       str - Full path to a file
# Outputs:
#       0 - Return value when the input is a folder
#       funct - Appropriate output path handler based on mapping in dictionary of file extensions
def get_file_type_handler(file_path):

    if not os.path.isfile(file_path):
        print(f"Log - \"{file_path}\" is a directory")
        return 0

    # Setup dictionary for supported extensions and their respective handler functions
    function_map = {
        '.jpg':     get_image_output_path,
        '.jpeg':    get_image_output_path,
        '.png':     get_image_output_path,
        '.gif':     get_image_output_path,
        '.bmp':     get_image_output_path,
        '.tiff':    get_image_output_path,
        '.heic':    get_image_output_path,
        
        '.mp4':     get_video_output_path,
        '.avi':     get_video_output_path,
        '.mov':     get_video_output_path,
        '.m4v':     get_video_output_path,

        '.xlsx':    get_excel_output_path,
        '.xls':     get_excel_output_path,
        '.csv':     get_excel_output_path,

        '.doc':     get_word_output_path,
        '.docx':    get_word_output_path,

        '.pptx':    get_ppt_output_path,

        '.pdf':     get_pdf_output_path
    }

    # Get extension of file_path
    file_path_extension = os.path.splitext(file_path)[1].lower()
    print(f"Log - Extension of \"{file_path}\" is \"{file_path_extension}\"")

    # Set the correct handler based on the dictionary above
    path_handler_function = function_map.get(file_path_extension)

    # If the extension exists in the dictionary, return the mapped function
    if (path_handler_function):
        return path_handler_function

    # If the extension does not exist in the dictionary, return the "other" function
    print(f"Log - \"{file_path}\" is a file type Other")
    return get_other_output_path
