# codesnippets

code snippets I can potentially use in the future as is or as example.

- [backup of dir with recursive function.py](https://github.com/lawfets/codesnippets/blob/main/backup%20of%20dir%20with%20recursive%20function.py)
  - making use of os, datetime and shutil, I made a recursive function to make the directories and copy the files in the base directory I chose. 
    If you want to make use of it (it works) you'll have to adapt the source and destination and you will also have to put in potential files that can cause problems.
- [shutilDistutilsDateTimeOs.py](https://github.com/lawfets/codesnippets/blob/main/shutilDistutilsDateTimeOs.py)  
  - This is also file-backup code but this time I used distutils.dir_util.copy_tree.
  - distutils.dir_util.copy_tree doesn't seem to have the an ignore attribute which makes it unusable to me as I have to skip a couple of .tmp files
    that are used by another process. Because of the useage of the tmp files, I get a **"permission denied"** error which throws me out of the program
    before it has done it's job. I don't think, I can fix this with distutils
