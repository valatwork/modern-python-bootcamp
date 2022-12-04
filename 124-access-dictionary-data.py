instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}


# accessing individual value

instructor["name"] # "Colt"

instructor["thing"] # KeyError



artist = {'first': 'Neil', 'last': 'Young'}
full_name = f"{artist['first']} {artist['last']}"
# full_name = artist["first"] + " " + artist["last"]
# full_name = "{} {}".format(artist["first"],artist["last"])
