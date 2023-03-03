## all

# Return True if all elements of the iterable are truthy (or if the iterable is empty)

all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True

## any

# Return True if any element of the iterable is truthy. If the iterable is empty, return False. 

any([0, 1, 2, 3]) # True

any([val for val in [1,2,3] if val > 2]) # True

any([val for val in [1,2,3] if val > 5]) # False

##

import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

## exercise

# Implement a function is_all_strings  that accepts a single iterable and returns True if it contains ONLY strings.  
# Otherwise, it should return false.  

is_all_strings(['a', 'b', 'c'])  #True

is_all_strings([2,'a', 'b', 'c'])  #False

is_all_strings(('hello', 'goodbye'))  #True

# is_all_strings solution 
# Using a Generator Expression

# I start by defining is_all_strings, which accepts a parameter called lst
# I call the built-in function all, passing in a generator expression that checks if the type of each item in the list is a str.  
def is_all_strings(lst):
    return all(type(l) == str for l in lst)

# Using a List Comprehension
# You can do the same thing, using a list comprehension instead of a generator expression: (just add list brackets around it)

def is_all_strings(lst):
    return all([type(l) == str for l in lst])
