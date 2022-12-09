# one parameter

# example 1

def square(num):
    return num**2
print(square(4))
print((square(8)))
# 16
# 64

# example 2

def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You")

sing_happy_birthday()
# TypeError: sing_happy_birthday() missing 1 required positional argument: 'name'

def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You")

sing_happy_birthday("Rashida")
sing_happy_birthday("Nicholas")

# two parameter

def add(a,b):
    return a+b

def multiply(first, second):
    return first * second

multiply(5,5) # 25
multiply(2,2) # 4

# naming parameters

## Not great
def print_full_name(string1, string2):
    return(f"Your full name is {string1} {string2}")

## Better

def print_full_name(first_name, last_name):
    return(f"Your full name is {first_name} {last_name}")

# parameters vs arguments

# A parameter is a variable in a method definition.
# When a method is called, the arguments are the data you pass into the method's parameters
# Parameter is variable in the declaration of function.
# Argument is the actual value of this variable that gets passed to function

## example 1

def sing_happy_birthday(name): # name is the parameter inside the function definition
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You")

sing_happy_birthday("Nicholas") # "Nicholas" is the argument

## example 2

# order matters

def divide(num1, num2):
    return num1/num2

print(divide(2,5))
print(divide(5,2))
