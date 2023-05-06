import os
import shutil
from_directory="C:/Users/Lenovo/Downloads"
listoffiles=os.listdir(from_directory)
#print(listoffiles)
for file in  listoffiles:
    name,extension=os.path.splitext(file)
    #print(name)
    print(extension)
