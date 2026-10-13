data=["Pen","Pencil","Book","Notes"]
with open("sample.txt","w") as file:
    file.write("\n".join(data))