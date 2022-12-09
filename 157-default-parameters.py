# Why have Default Params?
# Allows you to be more defensive
# Avoids errors with incorrect parameters
# More readable examples!

## example 1

def exponent(num, power):
    return num ** power

print(exponent(2,3)) # 8
print(exponent(3,2)) # 9 
print(exponent(7)) # 49

# TypeError: exponent() missing 1 required positional argument: 'power'

# fixed

def exponent(num, power=2):
    return num ** power

print(exponent(2)) # 8
print(exponent(3)) # 9 
print(exponent(7)) # 49

## example 2

def add(a,b):
    return a+b

add() # does not work!

# fixed

def add(a=10, b=20):
    return a+b

add() # 30
add(1,10) # 11

## example 3

def show_information(first_name="Colt", is_instructor=False):
    if first_name == "Colt" and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"

show_information() # "I really thought you were an instructor..."
show_information(is_instructor=True) # "Welcome back instructor Colt!"
show_information('Molly') # Hello Molly!


## example 4

def add(a,b):
    return a+b

def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b

math(2,2) # 4

math(2,2, subtract) # 0 

## example 4.1 - will not work, as the default value is not the LAST parameter, or everything should have a default parameter 

def add(a,b):
    return a+b

def math(fn=add, a,b):
    return fn(a,b)

def subtract(a,b):
    return a-b

math(2,2) # 4

math(2,2, subtract) # 0 

# SyntaxError: non-default argument follows default argument


