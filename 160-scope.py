# Scope
# Where our variables can be accessed!
# Variables created in functions are scoped in that function!

instructor = 'Colt' # this is not defined in the function but in the global scope

def say_hello():
    return f'Hello {instructor}'

say_hello() # 'Hello Colt'


def say_hello():
    instructor = 'Colt'
    return f'Hello {instructor}'
# the variable instructor is not available outside the above function
say_hello()

print(instructor) # NameError

# glocal scope

total = 0

def increment():
    total += 1
    return total

print(increment()) # UnboundLocalError: local variable 'total' referenced before assignment

# Lets us reference variables that were originally assigned on the global scope

total = 0

def increment():
    global total # specifies the reference to the global variable total
    total += 1
    return total

print(increment()) # 1

# nonlocal Scope

# Lets us modify a parent's variables in a child (aka nested) function

def outer():
    count = 0
    def inner():
        nonlocal count # this variable is not definited in inner or the global scope
        count += 1
        return count
    return inner()

