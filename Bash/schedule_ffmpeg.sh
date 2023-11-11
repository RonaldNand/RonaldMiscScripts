#!/bin/bash

function interrupt_script () {
	echo the script is terminated
	exit
}

function beginnings () {
	# Directory to scan
	directory="/path/to/your/directory"

	# Loop through video files in the directory
	for file in "$directory"/*.mp4; do
	  if [ -f "$file" ]; then
		codec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "$file")
		if [ "$codec" = "h264" ]; then
		  echo "x264 video detected: $file"
		fi
	  fi
}

trap interrupt_script SIGINT

while true
do
    echo Test
    sleep 1
done

