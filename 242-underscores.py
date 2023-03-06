## __name__

# Python specific methods

## _name

# convention for private properties/methords/attributes

## __name

# name mangling: this attribute/method specific to this class

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like turtles!" 
p = Person()

print(p.name)
print(p._secret)
# print(p.__msg) # AttributeError: 'Person' object has no attribute '__msg'

print(p._Person__msg)

'''
print(dir(p))

['_Person__msg', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_secret', 'name']
'''