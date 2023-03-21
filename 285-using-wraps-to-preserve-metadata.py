# Preserving Metadata

def log_function_data(fn):
    def wrapper(*args, **kwargs):
        '''I AM A WRAPPER FUNCTION'''
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    '''Adds two numbers together'''
    return x + y;

print(add(10,30))

# you are about to call add
# Here's the documentation: Adds two numbers together
# 40

print(add.__doc__)
print(add.__name__)
help(add)

# wrapper(*args, **kwargs)
#     I AM A WRAPPER FUNCTION

from functools import wraps
# wraps preserves a function's metadata
# when it is decorated

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass
    return wrapper

# code with decorator
from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''I AM A WRAPPER FUNCTION'''
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    '''Adds two numbers together'''
    return x + y;

print(add.__doc__)
print(add.__name__)
help(add)

# Adds two numbers together
# add
# Help on function add in module __main__:

# add(x, y)
#     Adds two numbers together
