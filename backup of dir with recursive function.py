#######################################################################
#backup of directory with recursive function.py:    This is a recursive function that can be used to recursively copy directories and files.
#                   I know I could have used shutil.copytree but I just wanted to test if I could do it by making
#                   the directories and copying the files.
#                   there is a piece of code in that can avoid certain file types like tmp files or other extensions

#   __author__      = "Stefaan Walleghem" aka lawfets
#   __copyright__   = "GNU GPLv3"
#   reason to make this: just for fun
#   written for python 3.9
#######################################################################


import os
import datetime
from shutil import copyfile
#I might use input to know source and destination but that's for the future
src= "C:\\wamp64" #these directories can be adapted as needed
specificTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
pathDir = "D:\\wamp64" + specificTime  #these directories can be adapted as needed
os.mkdir(pathDir)

def makeDirectories (source, destination):
    dirBool = False  #boolean needed to check if it's directory or if it's file
    for item in os.listdir(source):
        secSrcDir = os.path.join(source, item)

        dirBool = os.path.isdir(secSrcDir)
        if dirBool:
            secDstDir = destination + "\\" + item
            os.mkdir(secDstDir)
            dirBool = os.path.isdir(secDstDir)
            if dirBool:
                print(secDstDir)
                makeDirectories(secSrcDir, secDstDir) #recursion as I don't know how deep the directory layers go.
        else:
            secDstDir = destination + "\\" + item
            if secDstDir.endswith('.tmp'): #tmp files in this example were occupied by other program,
# it's possible to put other extension in this if statement
                print("This file was not copied due to permission rights")
            else:
                copyfile(secSrcDir,secDstDir)  #as directories are made on the fly, only files have to be copied
                print(secDstDir)

makeDirectories(src, pathDir)

