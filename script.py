import shutil
import sys,os

root = "/Users/mahyar/Library/Messages/Attachments/"
destination = "/Users/mahyar/Desktop/Gpic/"

if not os.path.exists(destination):
    os.makedirs(destination)

path = os.path.join(root, "targetdirectory")
for path, subdirs, files in os.walk(root):
    for name in files:
        print (os.path.join(path, name))
        shutil.copy2(os.path.join(path, name),os.path.join(destination, name))

