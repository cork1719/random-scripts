# I wrote this script because I had thousands of unsorted pictures in a folder making looking through them unwieldy. This is a quick way to sort them.

# Note: This is designed to be used on linux. To use on windows you must have the linux subsystem set up.

# To use, place this script in the directory and call it from the command line.

# requires exifread library to be installed.

import shutil, os, re, exifread, time, string
from pathlib import Path

DATE_REGEX = r'20\d\d[0-1]\d[0-3]\d'
IMAGE_TYPE_REGEX = r'(?i)\.png|\.dng|\.nef|\.cr2|\.jpg|\.jpeg'

# Loop through files in current directory
for filename in os.listdir():
    # Check if current file contains regexs
    datestring = re.search(DATE_REGEX, filename)
    isImage = re.search(IMAGE_TYPE_REGEX, filename)
    # Set flag for moving current file to false
    flag = False
    if datestring:
        # Get datestring from current file
        datestring = datestring.group(0)
        # Set flag to True since the current file matches datestring
        flag = True
    else:
        path = Path.cwd() / filename
        # Open current file
        file = open(str(path), 'rb')
        # Read current file's exif data
        tags = exifread.process_file(file, stop_tag='DateTimeOriginal')
        if 'EXIF DateTimeOriginal' in tags:
            # Set datestring and flag since the current file has the 'DateTimeOriginal' info
            datestring = str(tags['EXIF DateTimeOriginal'])[0:10]
            datestring = re.sub(r'[^\w]', '', datestring)
            flag = True
        elif isImage:
            # Set datestring and flag since the current file is an image
            datestring = str(time.strftime('%Y%m%d', time.localtime(path.stat().st_mtime)))
            flag = True
    # If flag is True attempt directory construction and movement of current file
    if flag == True:
        path = Path.cwd().parent / datestring[0:4] / datestring[4:6] / datestring
        path.mkdir(parents=True, exist_ok=True)
        # Check if file is already in directory. If not, move it there.
        path = path / filename
        if path.exists() == False:
            shutil.move('.//' + filename, str(path.parent))
