instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

## Accessing All Values in a Dictionary

for value in instructor.values():
    print(value)
    
# "Colt"
# True
# 4
# "Python"
# False
# "my favorite number!"


## Accessing All Keys in a Dictionary

for key in instructor.keys():
    print(key)

# name
# owns_dog
# num_courses
# favorite_language
# is_hilarious
# 44

## Accessing All Keys and Values

for key,value in instructor.items():
    print(key,value)

# name "Colt"
# owns_dog True
# num_courses 4
# favorite_language "Python"
# is_hilarious False
# 44 "my favorite number!"

## Accessing Individual Value

instructor["name"] # "Colt"

instructor["thing"] # KeyError

artist = {'first': 'Neil', 'last': 'Young'}
full_name = f"{artist['first']} {artist['last']}"
# full_name = artist["first"] + " " + artist["last"]
# full_name = "{} {}".format(artist["first"],artist["last"])
