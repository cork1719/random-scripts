# I wrote this script because I had thousands of unsorted pictures in a folder making looking through them unwieldy. This is a quick way to sort them.

import shutil, os, re

DATE_REGEX = '20([0-1]\d){2}[0-3]\d';

# Loop through files in current directory
for filename in os.listdir():
    # Check if current file contains regex
    datestring = re.search(DATE_REGEX, filename)
    if datestring:
        # Get datestring from current file
        datestring = datestring.group(0)
        # Check if directory for given date exists
        if os.path.isdir('..//' + datestring[0:4]) == False:
            os.makedirs('..//' + datestring[0:4])
        if os.path.isdir('..//' + datestring[0:4] + '//' + datestring[4:6]) == False:
            os.makedirs('..//' + datestring[0:4] + '//' + datestring[4:6])
        if os.path.isdir('..//' + datestring[0:4] + '//' + datestring[4:6] + '//' + datestring) == False:
            os.makedirs('..//' + datestring[0:4] + '//' + datestring[4:6] + '//' + datestring)
        # Check if file is already in directory. If not, move it there.
        if os.path.exists('..//' + datestring[0:4] + '//' + datestring[4:6] + '//' + datestring + '//' + filename) == False:
            shutil.move('.//' + filename, '..//' + datestring[0:4] + '//' + datestring[4:6] + '//' + datestring)