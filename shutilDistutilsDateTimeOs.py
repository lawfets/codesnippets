#######################################################################
#shutilDistutilsDateTimeOs.py:    made with shutil and distutils to backup some directories instead of making a full image.
#   __author__      = "Stefaan Walleghem" aka lawfets
#   __copyright__   = "GNU GPLv3"
#   reason to make this: because I needed it and I like it
#   written for python 3.9
#######################################################################

#this code will create problems with permission error
#need to use shutil.copytree with ignore_patterns to avoid .tmp files used by
#other program => therefore permission problem

from distutils import dir_util
import datetime
import os
from shutil import copyfile


specificTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
path = "E:\\backup" + specificTime + "\\"

baseDirBur = path + "bureaublad"
baseDirWWW = path + "www64"

try:
    os.mkdir(path)
except OSError as e:
    print("dir maken %s mislukt" % path)
else:
    print("dir maken %s gelukt" % path)

path1 = path + "bookmarks google\\"

baseFileGoogleBookmarks = path1 + "bookmarks"

try:
    os.mkdir(path1)
except OSError as e:
    print(e) #print("dir maken %s mislukt" % path1)
else:
    print("dir maken %s gelukt" % path1)

try:
    dir_util.copy_tree(r"C:\Users\stefaan\Desktop", baseDirBur, update = True, verbose = 1)
except PermissionError as e:
    print(e)
except Exception:
    print('kopie van bureaublad map mislukt')
else:
    print('kopie van bureaublad map compleet')
    
try:
    dir_util.copy_tree(r"C:\wamp64", baseDirWWW, update = True, verbose=1)
except Exception:
    print ('kopie van WWW map mislukt')
else:
    print ('kopie van WWW map compleet')

try:
    copyfile(r"C:\\Users\\stefaan\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks", baseFileGoogleBookmarks)
except Exception:
    print ('kopie van Google chrome bookmarks is mislukt')
else:
    print ('kopie van Google Chrome bookmarks is gelukt')

