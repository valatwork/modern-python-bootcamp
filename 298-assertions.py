''' 
We can make simple assertions with the assert keyword
assert accepts an expression
Returns None if the expression is truthy
Raises an AssertionError if the expression is falsy
Accepts an optional error message as a second argument
'''

# assert is a statement, not a function

## example 1

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

add_positive_numbers(1, 1) # 2
add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!

## example 2

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

print(add_positive_numbers(1, 1)) # 2
add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!

## example 3
def eat_junk(food):
	assert food in [
		"pizza", 
		"ice cream", 
		"candy", 
		"fried butter"
	], "food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))

# If a Python file is run with the -O flag, assertions will not be evaluated!
# Don't write code like this!

def do_something_bad(user):
    assert user.is_admin, "Only admins can do bad things!"
    destroy_a_bunch_of_stuff()
    return "Mua ha ha ha!"