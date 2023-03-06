'''
Custom Modules

You can import from your own code too
The syntax is the same as before
import from the name of the Python file

'''

# example 1

'''

file1.py

def fn():
    return "do some stuff"

def other_fn():
    return "do some other stuff"
    

import file1

file1.fn() # 'do some stuff'

file2.fn() # 'do some other stuff'

'''

# example 2

'''
apples.py

def offer():
	return "Hey do you like apples?"

def bake():
	return "Mmmm, pie..."

bananas.py

def peel():
	return "Here's a delicious banana!"

def dip_in_chocolate():
	return "Here's a delicious banana, dipped in chocolate!"

def sell():
	return "There's always money in the banana stand."
 
# Importing everythin in both modules:

# import bananas
# import apples

# print(apples.offer())

# print(bananas.dip_in_chocolate())


# Importing a single function from bananas:

from bananas import dip_in_chocolate as dip
print(dip())

'''
# exercise

'''
Your task is to write a function in the helpers.py file, and then call it from the exercise.py file.  More specifically:

In helpers.py, define a function called lucky_number()  that always returns the number 37.  That's it.   
It always returns 37, no matter what.

In exercise.py, import the helpers module.  
In order for the testing logic to work properly, don't use the 'as', or 'from' keywords when importing.  
Just do a plain old import.

From inside exercise.py, call the lucky_number function you defined in the helpers module. 
Save the result to a variable called num

The point of this exercise is to get comfortable working with multiple files, and defining custom modules.   
Because of that, the testing logic actually checks to see that your code is all in the correct filed rather than just checking if you got the right answer.
'''

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'



#Call the lucky_number function from your helpers module, and save the result to a variable called num