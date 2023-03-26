import subprocess
import os
from datetime import date
import sys
import string

# Set the target location for the output file
today = date.today()
backup_location = r"C:\Users\Ron\Desktop\Python Project\GeneralScripts\TestOutput"
backup_folder = f'{backup_location}\Tree_{today}'


drives = list(string.ascii_uppercase)

for letter in drives:
    command = f'tree {letter}:/ /f /a'
    output = subprocess.check_output(command, shell=True)
    if sys.getsizeof(output) > 100:
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
        file_name = f'{letter.upper()}_Drive_{today}.txt'
        with open(os.path.join(backup_folder,file_name),"wb") as f:
            f.write(output)
        print(f'Tree Listing Generated for Drive {letter}. This has been written to {file_name}')
    else:
        print(f'No Drive Found for Drive {letter}. Skipping')


