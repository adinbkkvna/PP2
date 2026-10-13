with open("sample.txt","r") as source:
    content=source.read()
with open("copy.txt","w") as file2:
    file2.write(content)