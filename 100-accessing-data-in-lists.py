# Like ranges, lists ALWAYS start counting at zero. So the first element lives at index 0.

friends = ["Ashley", "Matt", "Michael"]

print(friends[0]) # 'Ashley'
print(friends[2]) # 'Michael'
print(friends[3]) # IndexError

# You can use a negative number to index from the end of the list

print(friends[-1]) # 'Michael'
print(friends[-3]) # 'Ashley'
print(friends[-4]) # IndexError

# check if a value is in the list, case sensitive

friends = ["Ashley", "Matt", "Michael"]

"Ashley" in friends # True

"Colt" in friends # False

## exercise

'''
I'm having a party, and made a list of people I want to invite.  
Unfortunately, I'm a terrible friend and made a couple of spelling errors.  
Help me correct them!

Change "Hanna" to "Hannah" (there should be an 'h' at the end)

Change "Geoffrey" to "Jeffrey"

Change "aparna" to "Aparna" (capitalize it)

Hint: You can use the following syntax to change a value of an existing list element at the specific index position:

lst[0] = "NewValue"

Here, lst would represent the variable holding the list that we are modifying, 
and the 0 in square brackets would be the index number of the targetted list element that we are changing, 
and we would use the assignment operator = to set it to a new value. 
You can use this approach with the people list in this exercise to make the necessary modifications, as instructed above!
'''

# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[5] = "Aparna"