import os
import sys


file_names=os.listdir(sys.argv[1])
for files in file_names:
   print os.stat(files)

