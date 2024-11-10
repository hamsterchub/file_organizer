# Import Python libs
from datetime import datetime
from PIL import Image
from PIL. ExifTags import TAGS

# Import project files
from util_functions import os_join_path

# Logger
from app_logger import setup_logger
logger = setup_logger()


# Debugging function to parse exif data and log in debug mode
# Inputs:
#       exif_data object - exif data of an image
# Outputs:
#       None
def log_exif_data(exif_data):
    logger.debug(f"\n####################################")
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        logger.debug(f"\"{tag_name}\": \"{value}\"")
    logger.debug(f"####################################\n")
    return


# Logic to determine which exif data we want to organize our file by
# Inputs:
#       [<date obj>, <date obj>] - Dates to consider using for organizing an image file
# Return:
#       <date obj> - The chosen date object for organizing the image
def choose_exif_date(dates):
    chosen_date = min(dates)
    logger.debug(f"Chosen exif date for current file is \"{chosen_date}\"")
    return chosen_date


# Return directory structure in Year-Month-Day format given the metadata of an image for creation date/time
# Inputs:
#       exif_data object - exif data of an image to get various date/time metadata info on it
# Outputs:
#       str - "<yyyy>-<mm>-<dd>"
def get_image_exif_output(img_exif_data):
    date_original = img_exif_data.get(36867)   # DateTimeOriginal tag
    date_modified = img_exif_data.get(36866)   # DateModified tag

    # Setting up local variables to use for parsing exif metadata fields. Setting default date time to year far, far away for comparison
    bool_is_date_orig_or_mod = False    # Variable to be turned if either date_original or date_modified are valid
    date_orig_extract = datetime(9999, 1, 1, 1, 1, 1)
    date_mod_extract = datetime(9999, 1, 1, 1, 1, 1)

    if date_original:
        bool_is_date_orig_or_mod = True
        date_orig_extract = datetime.strptime(date_original, "%Y:%m:%d %H:%M:%S")
        logger.debug(f"DateTimeOriginal tag on this file: \"{date_orig_extract}\"")
    else:
        logger.debug(f"There is NOT a DateTimeOriginal tag on this file: \"{date_orig_extract}\"")
        
    if date_modified:
        bool_is_date_orig_or_mod = True
        date_mod_extract = datetime.strptime(date_modified, "%Y:%m:%d %H:%M:%S")
        logger.debug(f"Modified Date tag on this file: \"{date_mod_extract}\"")
    else:
        logger.debug(f"There is NOT a Modified Date tag on this file: \"{date_mod_extract}\"")

    if bool_is_date_orig_or_mod:
        # Return the appropriate date in yyyy-mm-dd format based on the logic of the choose_exif_date function
        return choose_exif_date([date_orig_extract, date_mod_extract]).strftime("%Y-%m-%d")

    logger.debug(f"There is NOT a DateTimeOriginal nor a DateModified tag on this file")
    return "no_date_time_tags"


# Set output directory appropriately for images (including error conditions)
# Inputs:
#       str - Full path to an image file
# Outputs:
#       False - If there was an issue opening the file. Otherwise...
#       str - Desired subdirectory to move image file to (ex. "images/2000-01-01")
def get_image_output_path(image_path):
    img_out_path = "images"
    try:
        # Open the media to get its creation date
        img = Image.open(image_path)
        exif_data = img._getexif()

        # Get the creation date from EXIF data if available
        if exif_data is not None:
            logger.debug(f"Valid exif data on this image: \"{image_path}\"")
            log_exif_data(exif_data)
            return img_out_path + get_image_exif_output(exif_data)

        # This code will execute if EXIF data is NOT available
        logger.debug(f"Invalid exif data on this image: \"{image_path}\"")
        return os_join_path(img_out_path, "no_exif_data")

    # This code will execute if there was an issue opening the file
    except Exception as e:
        logger.error(f"Error while opening \"{image_path}\": {e}")
        return False
