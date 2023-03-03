# There is a lambda for each value in the iterable
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda

# example 1

l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))

evens # [2,4]

# example 2 

names = ['austin', 'annthony', 'angel', 'billy']
a_names = filter(lambda: name: name[0]=='a', names)
list(a_names)

# example 3

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

## Combining filter and map

# Given this list of names:

names = ['Lassie', 'Colt', 'Rusty']

# Return a new list with the string
# "Your instructor is " + each value in the array, but only if the value is less than 5 characters

list(map(lambda name: f"Your instructor is {name}",
     filter(lambda value: len(value) < 5, names))) # this will run first and create a list containing only the names shorter than 5 characters

# ['Your instructor is Colt']

## What about List Comprehension?

# Given this list of names:

names = ['Lassie', 'Colt', 'Rusty']

# Return a new list with the string:
# "Your instructor is " + each value in the array, but only if the value is less than 5 characters

[f"Your instructor is {name}" for name in names if len(name) < 5]


# exercise

# Write a function called remove_negatives that accepts a list of numbers and returns a copy of the lists with all negative numbers removed. 
# se filter() in your implementation, not a list comprehension!

# remove_negatives([-1,3,4,-99])     #[3,4]

# remove_negatives([-7,0,1,2,3,4,5])      #[0, 1, 2, 3, 4, 5]

# remove_negatives([50,60,70])   #[50,60,70]

# HINTS

# Make sure you return a list!  Remember filter does not return a list! You have to convert the result to a list yourself.
# Note that 0 is not considered negative, so it should not be filtered out!

def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))