class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Adina","19")
print(p1.name)
print(p1.age)

class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=Person("Asiya")
p2=Person("Damir",25)
print(p1.name,p1.age)
print(p2.name,p2.age)

class Person:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country
p1=Person("Linda",30,"Astana","Kazakhstan")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)