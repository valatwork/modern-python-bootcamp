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

## exercise

'''
Given the provided dictionary of donations:

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0) 

Use a loop to calculate the total value of the donations.  Save the result to a variable called total_donations 
'''

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

total_donations = 0
 
for donation in donations.values():
 total_donations += donation
# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

## sum() solution

total_donations = sum(donation for donation in donations.values())

## better sum()

total_donations = sum(donations.values())
