# -------Using the Os package-------
print("Using Os package...")
import os
if os.path.exists("myfile.txt"):
    print("File Exist!")
else:
    print("File Doesn't Exist!")

# ------Using the pathlib module-------
print("Using pathlib module...")
from pathlib import Path
if Path("myfile.txt").exists(): # works for both file and folders
    print("File Exists!")
else:
    print("File Doesnt Exist!")

# ------Checking by opening the file------
print("Opening file...")
try: 
    with open('myfile.txt', 'r') as fh:
        print("File Exist!")
except FileNotFoundError: 
    print("File Doesn't Exist!")