'''
Handle Errors!

In Python, it is strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them. 
Let's see what that looks like.

'''

# example 1

try: 
    foobar
except NameError as err:
    print(err)

'''
THE BASIC SYNTAX:
try:
except:

try: 
    foobar
except:
    print("PROBLEM!")
print("after the try")

'''

# example 2

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Ricky"}
print(get(d, "city"))
d["city"]

# example 3

try: 
    colt
except:
    print("You tried to use a variable that was never declared!")
    
# example 4
# When you use try/except, make sure that a specific type of exception is being handled.

try: 
    colt
except NameError:
    print("You tried to use a variable that was never declared!")
    
# ​If you want to except a handful of exceptions, you can pass a tuple of errors into the except block as well:

try: 
    colt.hello
except (TypeError, AttributeError):
    print("That doesn't work with this thing.")
    

