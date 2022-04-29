# Program to create a duplicate of
# an already existing file
# by Alexander Graden

import os
D = r"C:\Users\agraden\Documents\VS Code\Python"

import shutil

print("Before copying file:")
print(os.listdir(D))

# src is the path of the source file
src = r"C:\Users\agraden\Documents\VS Code\Python\Will_list.py"

# dest is the path of the destination file
dest = r"C:\Users\agraden\Documents\VS Code\Python\Will_list_2.py"

path = shutil.copyfile(src,dest)

print("After copying file:")
print(os.listdir(D))

print("The path of the duplicate file is:")
print(path)