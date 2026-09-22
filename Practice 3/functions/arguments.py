def intro(name,age):
    print("My name is", name)
    print("I am", age,"years old")
intro("Adina","19")

#default
def welcome(name, message="Welcome"):
    print(message, name)
welcome("Adina")
welcome("Hello")

#keyword
def func(subject,time):
    print("I studied", subject)
    print(subject, "time is", time)
func(subject="math", time="16:00")

#positional
def func(animal,name):
    print("i have a", animal)
    print("My", animal+"'s name is", name)
func("cat","Maddy")

#mixing
def intro(fname,lname,age):
    print("My fname is", fname, "My lname is", lname, "I am", age)
intro("Adina","Kuralbek",age="19")


#list in func
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)
fruit_list=["apple", "banana", "orange"]
print_fruits(fruit_list)
