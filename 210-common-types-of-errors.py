'''
SytaxError

Occurs when Python encounters incorrect syntax (something it doesn't parse).
Usually due to typos or not knowing Python well enough

'''

def first: # SyntaxError

None = 1 # SyntaxError

return # SyntaxError

'''
NameError
This occurs when a variable is not defined, i.e. it hasn't been assigned

'''
test
# NameError: name 'test' is not defined

'''
TypeError
An operation or function is applied to the wrong type
Python cannot interpret an operation on two data types

'''
len(5)  
# TypeError: object of type 'int' has no len()

"awesome" + []  
# TypeError: cannot concatenate 'str' and 'list' objects

'''
IndexError

Occurs when you try to access an element in a list using an invalid index (i.e. one that is outside the range of the list or string):

'''
list = ["hello"]
list[2]
# IndexError: list index out of range

'''
ValueError
This occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value:

'''
int("foo")
# ValueError: invalid literal for int() with base 10: 'foo'

'''
KeyError
This occurs when a dictionary does not have a specific key:

'''
d = {}
d["foo"]
# KeyError: 'foo'

'''
AttributeError
This occurs when a variable does not have an attribute:

'''
"awesome".foo
# AttributeError: 'str' object has no attribute 'foo'
