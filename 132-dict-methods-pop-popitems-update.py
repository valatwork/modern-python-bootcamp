# pop takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed

d = dict(a=1,b=2,c=3)
d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
d # {'c': 3, 'b': 2}
d.pop('e') # KeyError
d.pop() # TypeError

# popitem removes a random key

d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() # ('d', 4)
d.popitem('a') # TypeError: popitem() takes no arguments (1 given)

# update updates keys and values in a dictionary with another set of key value pair

first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# let's overwrite an existng key
second['a'] = "AMAZING"

# if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

instructor = {'name': 'Colt', 'owns_dog': True, 'num_courses': 4, 'favorite_language': 'Python', 'is_hilarious': False, 44: 'my favorite number!'}
person = {"city": "Antigua"}
person = {'city': 'Antigua' 'name': 'Colt', 'owns_dog': True, 'num_courses': 4, 'favorite_language': 'Python', 'is_hilarious': False, 44: 'my favorite number!'} # different object
person['name'] = 'Evelia'
person = {'city': 'Antigua' 'name': 'Evelia', 'owns_dog': True, 'num_courses': 4, 'favorite_language': 'Python', 'is_hilarious': False, 44: 'my favorite number!'}
person.update(instructor) # will overwrite 'name' from person

## exercise

'''
I've provided you with a start dictionary called inventory. 

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE! 

Follow the instructions found in the comments:

1. Make a copy of inventory  and save it to a variable called stock_list  using a dictionary method we've covered

2. Add the value 18 to stock_list  under the key "cookie"

3. Remove 'cake' from stock_list  using a dictionary method we've learned
'''

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"

stock_list['cookie'] = 18


# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')