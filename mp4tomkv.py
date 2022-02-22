'''
   Module     : mp4tomkv.py
   Description: convert mp4 files in folder to mkv using program Mp42Mkvac3
   Author     : ricS

   History
     22 Feb 2022 - First Written
'''

import glob, os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askdirectory

root = Tk()
root.overrideredirect(1)
root.withdraw()

# constants
CVT_CMD = "C:\\ProgramData\\Mp42Mkvac3\\Mp42Mkvac3.exe"

path = askdirectory(title='Select Folder') # shows dialog box and return the path
print("Converting mp4 files in " + path)  

os.chdir(path)
path = path.replace("/", "\\")
for file in glob.glob("*.mp4"):
    print("--- " + file)
    cmd = CVT_CMD + " " + path + "\\" + file
    #print(cmd)
    p = subprocess.Popen(cmd, shell=True)
    retval = p.wait()

