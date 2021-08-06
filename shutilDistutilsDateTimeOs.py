#######################################################################
#shutilDistutilsDateTimeOs.py:    made with shutil and distutils to backup some directories instead of making a full image.
#   __author__      = "Stefaan Walleghem" aka lawfets
#   __copyright__   = "GNU GPLv3"
#   reason to make this: because I needed it and I like it
#   __pythonv: 3.9
#######################################################################

#this code will create problems with permission error
#need to use shutil.copytree with ignore_patterns to avoid .tmp files used by
#other program => therefore permission problem
# code in here can be changed and made more decent but I just want to remember the concept

from distutils import dir_util
import datetime
import os
from shutil import copyfile


specificTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
basePath = "E:\\backup" + specificTime + "\\"

baseDirBur = basePath + "bureaublad" #changed from path to basePath as path is part of os module
baseDirWWW = basePath + "www64"

try:
    os.mkdir(basePath)
except OSError as e:
    print("dir maken %s mislukt" % basePath)
else:
    print("dir maken %s gelukt" % basePath)

path1 = basePath + "bookmarks google\\"

baseFileGoogleBookmarks = path1 + "bookmarks"

try:
    os.mkdir(path1)
except OSError as e:
    print(e)
else:
    print("dir maken %s gelukt" % path1)
# backup of my desktop directory as I keep a lot on the desktop
try:
    dir_util.copy_tree(r"C:\Users\stefaan\Desktop", baseDirBur, update = True, verbose = 1)
except PermissionError as e:
    print(e)
except Exception:
    print('kopie van bureaublad map mislukt')
else:
    print('kopie van bureaublad map compleet')
# backup of the wamp directory so I don't lose my webpages
try:
    dir_util.copy_tree(r"C:\wamp64", baseDirWWW, update = True, verbose=1)
except Exception:
    print ('kopie van WWW map mislukt')
else:
    print ('kopie van WWW map compleet')
# backup of the bookmarks file from google chrome
try:
    copyfile(r"C:\\Users\\stefaan\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks", baseFileGoogleBookmarks)
except Exception:
    print ('kopie van Google chrome bookmarks is mislukt')
else:
    print ('kopie van Google Chrome bookmarks is gelukt')

