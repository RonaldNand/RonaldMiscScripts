import subprocess
import os

# Set the relative path to the folder containing the folders to be zipped
path = r"C:\Users\Ron\Desktop\TEMP\Comic"

# Loop through all the folders in the path
for folder in os.listdir(path):
    if os.path.isdir(os.path.join(path, folder)):
        input_file = f'"{os.path.join(path, folder)}"'
        output_file = f'"{os.path.join(path, folder + ".cbz")}"'
        new_name= output_file.replace(".zip", ".cbz")
        subprocess.run(f"7z a -tzip {output_file} {input_file}")

