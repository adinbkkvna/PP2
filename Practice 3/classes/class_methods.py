#method
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Hello, my name is"," " + self.name)
p1=Person("Adina") 
p1.greet()

#method with parameter
class Calculator:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
calc=Calculator()
print(calc.add(5,2))
print(calc.multiply(4,6))

#method accessing properties
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"{self.name} is {self.age} years old"
p1=Person("Asel",54)
print(p1.info())

#str
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)