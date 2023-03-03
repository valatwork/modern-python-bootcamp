# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first 
# letter of each name in the list.  
# I would use a list comprehension, though you could also loop over manually.

person = ["Elie", "Tim", "Matt"] # this creates a global variable, masking the local variable

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]

# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  
# Another good candidate for a list comp.

val = [1,2,3,4,5,6] # this creates a global variable, masking the local variable

answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
