'''
Reading Files
-You can read a file with the open function
-open returns a file object to you
-You can read a file object with the read method
'''

# story.txt

This short story is really short.

# reading_files.py

file = open("story.txt")
file.read()

'''
Cursor Movement

Python reads files by using a cursor (This is like the cursor you see when you're typing)
After a file is read, the cursor is at the end
To move the cursor, use the seek method
To read only part of a file, pass a number of characters into read, or use readline
To get a list of all lines, use readlines

'''

'''
Closing a File

You can close a file with the close method
You can check if a file is closed with the closed attribute
Once closed, a file can't be read again
Always close files - it frees up system resources!
'''