# and:   truthy if both a AND b are true (logical conjunction)
if a and b:
    print(c)

# or:    truthy if either a OR b are true (logical disjunction)
if am_tired or is_bedtime:
    print("go to sleep")
# not:   truthy if the opposite of a is true (logical negation)
if not is_weekend:
    print("go to work")


# print("Enter your age")
# age = int(input())
# if age > 2 and age < 6:
#     print("You get a discount")


# city = input("Where do you live?")

# if city == "los angeles" or city == "san francisco":
#     print("YOU LIVE IN CALIFORNIA!")
# else:
#     print("YOU LIVE SOMEWHERE ELSE")

# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# print(food)
if food == ('apple' or 'grape'):
    print('fruit')
elif food == ('bacon' or 'steak'):
    print('meat')
else:
    print('yuck')


# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# NO TOUCHING ======================================
# from random import choice
# food = choice(['apple','grape', 'bacon', 'steak', 'worm'])
# # NO TOUCHING ======================================
 
 
# # YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# if food == 'apple' or food == 'grape':
#     print ("fruit")
# elif food == 'bacon' or food == 'steak':
#     print("meat")
# else:
#     print("yuck")
