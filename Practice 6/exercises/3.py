import os
path="practice/sample.txt"

if os.path.exists(path):
    print("Filename:",os.path.basename(path))
    print("Directory:",os.path.dirname(path))
else:
    print("doesn't exist")