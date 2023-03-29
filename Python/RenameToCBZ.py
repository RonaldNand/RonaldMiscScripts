import os

# Change to the directory containing the files
os.chdir(r'C:\Users\Ron\Downloads\JDownloader')

# Get a list of all files in the directory
files = os.listdir()

# Loop through the files and rename any .zip files to .cbz
for file in files:
    if file.endswith('.zip'):
        # Construct the new file name
        new_name = file[:-3] + 'cbz'
        # Rename the file
        os.rename(file, new_name)