# codesnippets

code snippets I can potentially use in the future as is or as example.

-[asterixBeforeAttributeInFunction.py](https://github.com/lawfets/codesnippets/blob/main/asterixBeforeAttributeInFunction.py)
  - using *names for an attribute of a function where I don't know the amount of items in the attribute.
    As soon as the asterix is added, the attribute seems to become a tuple where it first was a string or an int.
- [backup of dir with recursive function.py](https://github.com/lawfets/codesnippets/blob/main/backup%20of%20dir%20with%20recursive%20function.py)
  - making use of os, datetime and shutil, I made a recursive function to make the directories and copy the files in the base directory I chose.
    If you want to make use of it (it works) you'll have to adapt the source and destination and you will also have to put in potential files that can cause problems.
- [ifElseInReturn](https://github.com/lawfets/codesnippets/blob/main/ifElseInReturn.py)
  - If else statement can be nested in the return statement.
- [itertoolChainObjectRange.py](https://github.com/lawfets/codesnippets/blob/main/iterToolChainObjectRange.py)
  - a generator object keeps in memory until we go through the body ones. after that you get an empty .
- [shutilDistutilsDateTimeOs.py](https://github.com/lawfets/codesnippets/blob/main/shutilDistutilsDateTimeOs.py)
  - This is also file-backup code but this time I used distutils.dir_util.copy_tree.
  - distutils.dir_util.copy_tree doesn't seem to have the an ignore attribute which makes it unusable to me as I have to skip a couple of .tmp files
    that are used by another process. Because of the useage of the tmp files, I get a **"permission denied"** error which throws me out of the program
    before it has done it's job. I don't think, I can fix this with distutils
- [useForRange.py](https://github.com/lawfets/codesnippets/blob/main/useForRange.py
  - basic usage of range
- [weirdUseOfLambda.py](https://github.com/lawfets/codesnippets/blob/main/weirdUseOfLambda.py)
  - use of ternary operator with lambda functions (anonymous functions)
