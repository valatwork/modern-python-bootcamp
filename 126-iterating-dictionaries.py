instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

for value in instructor.values():
    print(value)

# "Colt"
# True
# 4
# "Python"
# False
# "my favorite number!"

for key in instructor.keys():
    print(key)

# name
# owns_dog
# num_courses
# favorite_language
# is_hilarious
# 44

for key,value in instructor.items(): # the name doesn't matter
    print(key,value)

# name "Colt"
# owns_dog True
# num_courses 4
# favorite_language "Python"
# is_hilarious False
# 44 "my favorite number!"

for key,value in instructor.items():
    print(f"key is {key} and value is {value}")
    
# key is name and value is Colt
# key is owns_dog and value is True
# key is num_courses and value is 4
# key is favorite_language and value is Python
# key is is_hilarious and value is False
# key is 44 and value is my favorite number!