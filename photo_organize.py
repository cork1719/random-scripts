# I wrote this script because I had thousands of unsorted pictures in a folder making looking through them unwieldy. This is a quick way to sort them.

# Note: This is designed to be used on linux. To use on windows you must have the linux subsystem set up.

# To use, place this script in the directory and call it from the command line.

import shutil, os, re
from pathlib import Path

DATE_REGEX = r'20\d\d[0-1]\d[0-3]\d'

# Loop through files in current directory
for filename in os.listdir():
    # Check if current file contains regex
    datestring = re.search(DATE_REGEX, filename)
    if datestring:
        # Get datestring from current file
        datestring = datestring.group(0)
        path = Path.cwd().parent / datestring[0:4] / datestring[4:6] / datestring
        path.mkdir(parents=True, exist_ok=True)
        # Check if file is already in directory. If not, move it there.
        path = path / filename
        if path.exists() == False:
            shutil.move('.//' + filename, str(path.parent))