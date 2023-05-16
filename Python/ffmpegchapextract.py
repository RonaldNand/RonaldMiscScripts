
#ffprobe -i test.mp4 -show_chapters -print_format csv > test.csv

import subprocess
import datetime
import csv

def convert_seconds_to_timecode(seconds):
    time = datetime.timedelta(seconds=seconds)
    timecode = str(time)
    timecode = timecode.split(".")[0]
    return timecode

# Define the ffprobe command as a list of arguments
ffprobe_args = ['ffprobe', '-i', 'test.mp4', '-show_chapters', '-print_format', 'csv']

# Execute the ffprobe command using subprocess
with open('test.csv', 'w') as output_file:
    subprocess.run(ffprobe_args, stdout=output_file)

with open('test.csv','r') as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        # Access each row's data using indexing
        title = row[7]
        start = convert_seconds_to_timecode((int(row[3]) * eval(row[2])))
        end = convert_seconds_to_timecode((int(row[5]) * eval(row[2])))
        #print("name " + row[7] + " start " + start + " end " + end)
        print(start + " : " + title)



