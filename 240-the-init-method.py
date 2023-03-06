# Classes in Python can have a special __init__ method, which gets called every time you create an instance of the class (instantiate).
# There are some special cases where __init__ is not needed

# example 1

class User:
    def __init__(self,first): # this is the standard, it could be called anything
        # print("A NEW USER HAS BEEN MADE!") this is just to show what happens
        self.name = first

user1 = User("Joe")
user2 = User("Blanca")
# to access specific attributes on an instance, run instance.attribute_name
print(user1.name)

# example 1 continued

class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last)
print(user2.first, user2.last)

## instantiating a class

# Creating an object that is an instance of a class is called instantiating a class.

## self

# The self keyword refers to the current class instance.

# self must always be the first parameter to __init__ and any methods and properties on class instances.

# You never have to pass it directly when calling instance methods, including __init__.

# example 2

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

v = Vehicle("Honda", "Civic", 2017)

# In this case, v becomes a Honda Civic, a new instance of Vehicle

# v
# <__main__.Vehicle at 0x10472f5c0>
# v.make
# 'Honda'
# v.model
# 'Civic'
# v.year
# 2017



