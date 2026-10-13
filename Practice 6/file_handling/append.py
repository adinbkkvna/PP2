with open("sample.txt", "a") as file:
    file.write("\nI am from Almaty")

with open("sample.txt","r") as file:
    print(file.read())