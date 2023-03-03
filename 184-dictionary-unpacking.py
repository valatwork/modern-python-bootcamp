# Dictionary Unpacking

# Using ** as an Argument:
# We can use ** as an argument to a function to "unpack" dictionary values into keyword arguments

# example 1

def display_names(first, second):
    return f"{first} says hello to {second}"

names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..
# TypeError: display_names() missing 1 required positional argument: 'second'

display_names(**names) # 'Colt says hello to Rusty'

# example 2

def add_and_multiply_numbers(a,b,c):
    return a + b * c
data = dict(a=1,b=2,c=3)

# add_and_multiply_numbers(data) # nope..
#TypeError: add_and_multiply_numbers() missing 2 required positional arguments: 'b' and 'c'
add_and_multiply_numbers(**data) # 7

# example 2 with **kwargs

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF")
    print(kwargs)
    
data = dict(a=1, b=2, c=3,d=55, name='Tony')
add_and_multiply_numbers(**data)
# 7
# OTHER STUFF
# {'d': 55, 'name': 'Tony'}

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF")
    print(kwargs)
    
data = dict(a=1, b=2, c=3,d=55, name='Tony')
add_and_multiply_numbers(**data, cat="blue")

# 7
# OTHER STUFF
# {'d': 55, 'name': 'Tony', 'cat': 'blue'}