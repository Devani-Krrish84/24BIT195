import os
import shutil

source_file = r"c:\Users\devan\Python Library\Python\File Handling\q3.py"
target_directory = r"c:\Users\devan\Python Library\Python\File Handling\NewSubdirectory"

if not os.path.exists(target_directory):
    os.makedirs(target_directory)

shutil.copy(source_file, target_directory)