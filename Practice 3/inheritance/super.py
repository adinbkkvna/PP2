class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self, name,university):
        super().__init__(name)
        self.university=university
student=Student("Adina","KBTU")
print("Name",student.name)
print("University",student.university)