class Student:
    university="KBTU"

    def __init__(self,name):
        self.name=name

student1=Student("Adina")
student2=Student("Dana")
print(student1.university)
print(student2.university)
#instance variable
student1.name="Aruzhan"
print(student1.name)
print(student2.name)