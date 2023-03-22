# A data structure that consists of key value pairs.
# We use the keys to describe our data and the values to represent the data


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

cart = [{'name': 'cat litter', 'quantity': 3}] # list of dictionaries

cat = {'name': 'blue', 'age': 3.5, 'isCute': True}

# second method

another_dictionary = dict(key = 'value')
another_dictionary # {'key': 'value'}

cat2 = dict(name='kitty', age=0.5)


# addendum: create a dictionary from a nested list

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = {x[0]:x[1] for x in person}

dict(person) # this works as we have a list of pairs


'''
Create a dictionary called user_info  and add at least 3 key value pairs to it (totally up to you what they are)
'''
user_info = {'city': 'Utrecht', 'job': 'ITFSE', 'house': 'apartment'}