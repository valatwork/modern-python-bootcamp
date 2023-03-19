'''
A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).

In Python, inheritance works by passing the parent class as an argument to the definition of a child class:

'''

class Animal:
    def make_sound(self, sound):
        print(sound)

    cool = True

# Cat class inherits from Animal
class Cat(Animal):
    pass

gandalf = Cat()
gandalf.make_sound("meow")  # meow
gandalf.cool  # True

# Make a new cat instance
blue = Cat()

# Because of inheritance, a Cat has access to:
blue.make_sound("Meow")
print(blue.cool)

#blue is both a Cat and Animal (and base object)
print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
print(isinstance(blue, object))