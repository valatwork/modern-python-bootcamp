# ordered list of data

# synthax
numbers = (1, 2, 3, 4)

## it is immutable!
x = (1,2,3)
3 in x # True
x[0] = "change me!" # TypeError: 'tuple' object does not support item assignment

## example 1

alphabet = ('a', 'b', 'c', 'd')


# Why use a Tuple?
# Tuples are faster than lists
# It makes your code safer (from bugs)
# Valid keys in a dictionary
# Some methods return them to you - like .items() when working with dictionaries!


# Create using () or the tuple function
# Accessing is just like a list!

first_tuple = (1, 2, 3, 3, 3)

first_tuple[1] // 2
first_tuple[2] // 3
first_tuple[-1] // 3

second_tuple = tuple(5, 1, 2)

second_tuple[0] # 5
second_tuple[-1] # 2

## example 2

# locs = {[35,39]: 'Tokyo Office'}
# TypeError: unhashable type: 'list'
# a list cannot be a dict key
# a tuple can be a dict key

locations = {
    (35.6895, 39.6917): 'Tokyo Office',
    (40.7128, 74.0060): 'New York Office',
    (37.7749, 122.4194): 'San Francisco Office'
}
locations[(37.7749, 122.4194)]

## example 3

# some dict methods like .items() return tuples

cat = {'name': 'biscuit', 'age': 0.5, 'favorite_toy': 'my chapstick'}
cat.items()
dict_items([('name', 'biscuit'), ('age', 0.5), ('favorite_toy', 'my chapstick')]) # each item in there is a tuple, as the values will not change

# tuples can be nested

nums = (1,2,3,(4,5),6,7)
nums[3]
#(4,5)

nums[3][1]
# 5

# slices work too

nums = (1,2,3,(4,5),6,7)
nums[0:]
# (1,2,3,(4,5),6,7)
nums[0:4]
# (1,2,3,(4,5))
nums[0:4:2]
# (1,3)