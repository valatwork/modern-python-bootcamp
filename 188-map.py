# A standard function that accepts at least two arguments, a function and an "iterable"

# iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)

# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

nums = [1, 2, 3, 4]

doubles = list(map(lambda x: x * 2, nums))

evens # [2, 4, 6, 8]

# maps can only be iterated once

names = [
    {'first':'Rusty', 'last': 'Steele'}, 
    {'first':'Colt', 'last': 'Steele', }, 
    {'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))

first_names # ['Rusty', 'Colt', 'Blue']

# exercise

# Write a function called decrement_list  that accepts a single list of numbers as a parameter.  
# It should return a copy of the list where each item has been decremented by one. Use map to do this! For example:

# decrement_list([1,2,3])   #[0,1,2]

# decrement_list([20,14,11])  #[19,13,10]

# Tips:

# Remember map doesn't return a list on its own.  decrement_list , however, should return a list.
# You can either pass map another name function or use a lambda.  A lambda is preferable, even if it is a little scary looking.

def decrement_list(l):
    return list(map(lambda n: n-1, l))