import os
for name in os.listdir("."):
    if name.endswith("txt"):
        print(name)
