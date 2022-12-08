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
