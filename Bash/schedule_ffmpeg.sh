#!/bin/bash

# Use the command: pkill -QUIT <name_of_script_file>
# To send interrupt to process

lock_file="/tmp/my_script.lock"

run_script=true

# Check if the lock file exists
if [ -e "$lock_file" ]; then
    echo "Another iteration of the script is already running. Exiting."
    exit 1
else
    # Create the lock file
    touch "$lock_file"
fi

# Set Script FLAG to false on SIGQUIT Signal
function finish_script () {
	run_script=false
	echo "The script will terminate upon completion of current task"
}

trap finish_script SIGQUIT


# Include Code Here
for i in {1..300}
do
    sleep 1
	echo "Number: $i"
	if ! $run_script; then 
		rm -f "$lock_file"
		exit 0
	fi
done

# Upon Completion remove the lock file 

rm -f "$lock_file"
echo "All Tasks Complete!"

exit 0 
