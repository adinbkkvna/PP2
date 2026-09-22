class Animal:
    def make_cound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog says wof" )

dog=Dog()
dog.make_sound()