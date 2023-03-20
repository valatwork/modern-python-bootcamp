'''
Method Resolution Order (MRO)

Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, 
which is the order in which Python will look for methods on instances of that class.

You can programmatically reference the MRO three ways:

__mro__ attribute on the class
use the mro() method on the class
use the builtin help(cls) method

'''

## example 1

Penguin.__mro__ 

# (<class 'multiple.Penguin'>, <class 'multiple.Aquatic'>, 
#  <class 'multiple.Ambulatory'>, <class 'object'>)

Penguin.mro() 

# [__main__.Penguin, __main__.Aquatic, __main__.Ambulatory, object]

help(Penguin) # best for HUMAN readability -> gives us a detailed chain 


## example 2

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    def do_something(self):
        print ("Method Defined In: B")

class C(A):
    def do_something(self):
        print ("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print ("Method Defined In: D")

thing = D()
thing.do_something() # Method Defined In: D

## example 3

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    def do_something(self):
        print ("Method Defined In: B")

class C(A):
    def do_something(self):
        print ("Method Defined In: C")

class D(B,C):
    pass
    # def do_something(self):
    #     print ("Method Defined In: D")

# print(D.__mro__) (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# print(D.mro()) [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
help(D)

'''
Help on class D in module __main__:

class D(B, C)
 |  Method resolution order:
 |      D
 |      B
 |      C
 |      A
 |      builtins.object
 |  
 |  Methods inherited from B:
 |  
 |  do_something(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


'''

## example 4

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    def do_something(self):
        print ("Method Defined In: B")

class C(A):
    def do_something(self):
        print ("Method Defined In: C")

class D(B,C):
    pass
    # def do_something(self):
    #     print ("Method Defined In: D")

thing = D()
thing.do_something() # Method Defined In: B

## example 5

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    pass
    # def do_something(self):
    #     print ("Method Defined In: B")

class C(A):
    def do_something(self):
        print ("Method Defined In: C")

class D(B,C):
    pass
    # def do_something(self):
    #     print ("Method Defined In: D")

thing = D()
thing.do_something() # Method Defined In: C

## example 5

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    pass
    # def do_something(self):
    #     print ("Method Defined In: B")

class C(A):
    pass
    # def do_something(self):
    #     print ("Method Defined In: C")

class D(B,C):
    pass
    # def do_something(self):
    #     print ("Method Defined In: D")

thing = D()
thing.do_something() # Method Defined In: A

## example 5

class A:
    pass
    # def do_something(self):
    #     print ("Method Defined In: A")

class B(A):
    pass
    # def do_something(self):
    #     print ("Method Defined In: B")

class C(A):
    pass
    # def do_something(self):
    #     print ("Method Defined In: C")

class D(B,C):
    pass
    # def do_something(self):
    #     print ("Method Defined In: D")

thing = D()
thing.do_something() # Method Defined In: A

'''
AttributeError                            Traceback (most recent call last)
Cell In[3], line 22
     18     # def do_something(self):
     19     #     print ("Method Defined In: D")
     21 thing = D()
---> 22 thing.do_something() # Method Defined In: A

AttributeError: 'D' object has no attribute 'do_something'

'''

## example 7

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    def do_something(self):
        print ("Method Defined In: B")

class C(A):
    def do_something(self):
        print ("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print ("Method Defined In: D")
        super().do_something()
thing = D()
thing.do_something() 
# Method Defined In: D
# Method Defined In: B

## example 8

class A:
    def do_something(self):
        print ("Method Defined In: A")

class B(A):
    def do_something(self):
        print ("Method Defined In: B")
        super().do_something()

class C(A):
    def do_something(self):
        print ("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print ("Method Defined In: D")
        super().do_something()
thing = D()
thing.do_something()
# Method Defined In: D
# Method Defined In: B
# Method Defined In: C