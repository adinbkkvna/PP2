names=["Adina","Amina","Alina"]
for index in enumerate(names):
    print(index,names)


names=["Adina","Amina","Alina"]
points=[85,90,70]
for names,points in zip(names,points):
    print(names,points)