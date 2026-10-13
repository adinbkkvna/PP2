import os
delete="new.txt"
if os.path.isfile(delete) and os.access(delete, os.W_OK):
    os.remove(delete)
else:
    print("File does not exist")