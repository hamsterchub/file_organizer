# file_organizer
Little project I developed to help organize the misc files for my family PCs

The program flows like this:
1. Define the following directories directly in the source code
    input_dir
    output_dir
2. The program will begin to traverse the input_dir
3. The program is smart enough to traverse nested directories. Recursive calls to run_main will be used to traverse nested directories
4. The program will sort your data according to the handler functions. The handler functions define the names of the nested output directories to create
5. More complex handler modules exist for file types with lots of metadata, like images. Most handler functions are simple method calls with str return at the moment

Required setup:
1. Install python
2. python -m pip install --upgrade pip
3. python -m pip install Pillow

Program Files:
1. app_logger.py - Logging solution
2. util_functions.py - OS calls, Debug printer, Duplicte file handler
3. handler_functions.py - Determine file type and invoke correct file processor, non-image file processors
3. image_handler.py - Called by handler_functions.py for files with "image" type extensions (defined in handler_functions)
3. file_organizer.py - Main invocation, folder definitions/setup, loop through directory for processing images (recursively as needed)
