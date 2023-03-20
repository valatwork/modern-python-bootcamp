'''
Polymorphism

A key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph).

While a formal definition of polymorphism is more difficult, here are two important practical applications:

1. The same class method works in a similar way for different classes

'''
Cat.speak()  # meow
Dog.speak()  # woof
Human.speak()  # yo

'''
2. The same operation works for different kinds of objects

'''

sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

len(sample_list)
len(sample_tuple)
len(sample_string)

'''
Polymorphism & Inheritance

1. The same class method works in a similar way for different classes

A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. 
This is called method overriding.

Each subclass will have a different implementation of the method.
If the method is not implemented in the subclass, the version in the parent class is called instead.

'''
## example 1

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"
    
class Fish(Animal):
    pass

d = Dog()
print(d.speak())
f = fish
print(f.speak()) # NotImplementedError("Subclass needs to implement this method")

## example

class Aquatic:
  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
  def __init__(self,name):
    print("PENGUIN INIT!")
    super().__init__(name=name)
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")

# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ??

'''
Special Methods

2. (Polymorphism) The same operation works for different kinds of objects

How does the following work in Python?

'''

8 + 2  # 10
"8" + "2"  # 82

''' 
The answer is "special methods"!

Python classes have special (also known as "magic") methods, that are dunders (i.e. double underscore-named). 

These are methods with special names that give instructions to Python for how to deal with objects.

'''