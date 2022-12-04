instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

# does the key exist

"name" in instructor # True
"awesome" in instructor # False

# does the value exist

"Colt" in instructor.values() # True
"Nope!" in instructor.values() # False