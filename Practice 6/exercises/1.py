import os
path="."

for name in os.listdir(path):
    full_path=os.path.join(path,name)

    if os.path.isdir(full_path):
        print("directory:",name)
    elif os.path.isfile(full_path):
        print("file:",name)
print("all items",os.listdir(path))