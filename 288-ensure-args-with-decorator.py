from functools import wraps

def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed! sorry :(")
		return fn(*args, **kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")

greet(name="Tony")

# exercise 1

'''
Write a function called double_return which accepts a function and returns another function. 
double_return should decorate a function by returning two copies of the inner function's return value inside of a list.

'''

from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

# exercise 2

'''
Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. 
The function passed to it should only be invoked if there are fewer than three positional arguments passed to it. 
Otherwise, the inner function should return "Too many arguments!"

'''

from functools import wraps
 
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper


# exercise 3

'''
Write a function called only_ints which accepts a function and returns another function. 
The function passed to it should only be invoked if all of the arguments passed to it are integers. 
Otherwise the inner function should return "Please only invoke with integers.".

'''

from functools import wraps
 
def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

# exercise 4

'''
Write a function called ensure_authorized which accepts a function and returns another function. 
The function passed to it should only be invoked if there exists a keyword argument with a name of "role" and a value of "admin". 
Otherwise, the inner function should return "Unauthorized"
'''

from functools import wraps
 
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper