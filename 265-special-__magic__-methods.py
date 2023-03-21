# Special Methods Example

# The + operator is shorthand for a special method called __add__() that gets called on the first operand.

8 + 2  # 10

# If the first (left) operand is an instance of int, __add__() does mathematical addition. If it's a string, it does string concatenation.

"8" + "2"  # 82

# Therefore, you can declare special methods on your own classes to mimic the behavior of builtin objects, like so using __len__:

class Human:
    def __init__(self, height):
        self.height = height  # in inches

    def __len__(self):
        return self.height

Colt = Human(60)
len(Colt)  # 60

# String Representation

# The most common use-case for special methods is to make classes "look pretty" in strings.

# By default, our classes look ugly:

class Human:
    pass

colt = Human()
print(colt)  # <__main__.Human at 0x1062b8400>

# We can use special methods to make it look way better!

# The __repr__ method is one of several ways to provide a nicer string representation:

class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name
        
dude = Human()
print(dude)  # "somebody"
colt = Human(name="Colt Steele")
print(f"{colt} is totally rad (probably)") 
# "Colt Steele is totally rad (probably)"

# There are also several other dunders to return classes in string formats (notably __str__ and __format__), and choosing one is a bit complicated!

## example

from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "CANT MULTIPLY!"
	


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))
# triplets = j * 3

# kevin and jessica have triplets!
triplets = (k + j) * 3
print(triplets)



