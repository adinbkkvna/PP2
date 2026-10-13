import os
path=input("file path:")
if os.path.exists(path):
    if os.path.isfile(path) and os.access(path,os.W_OK):
        os.remove(path)
        print("file deleted")
    else:
        print("path is not writable")
else:
    print("does not exist")