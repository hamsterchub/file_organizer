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
