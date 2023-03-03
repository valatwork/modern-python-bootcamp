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