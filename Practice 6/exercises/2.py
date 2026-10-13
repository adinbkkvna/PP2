import os
path="sample.txt"
print("exists",os.path.exists(path))
print("readable",os.access(path,os.R_OK))
print("writable",os.access(path,os.W_OK))
print("executable",os.access(path,os.X_OK))