## exercise 1

'''
Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first 
letter of each name in the list.  
I would use a list comprehension, though you could also loop over manually.
'''

person = ["Elie", "Tim", "Matt"] # this creates a global variable, masking the local variable

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]

## exercise 2
'''
Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  
Another good candidate for a list comp.
'''

val = [1,2,3,4,5,6] # this creates a global variable, masking the local variable

answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

## exercise 4

'''
1. Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer, which is a new list that is the intersection of the two. Your output should be [3,4] . 
Hint: use the in  operator to test whether an element is in a list.  For example:  5 in [1,5,2]  is True.  3 in [1,5,2]  is False.

2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2, 
which is a new list with each word reversed and in lower case (use a slice to do the reversal!) Your output should be ['eile', 'mit', 'ttam'] 
'''

[1,2,3,4]
[3,4,5,6]

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]


["Elie", "Tim", "Matt"]
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

## exercise 5

'''
For all the numbers between 1 and 100(including 100), create a variable called answer, 
which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
USE A LIST COMPREHENSION.
'''
answer = [val for val in range(1,101) if val % 12 == 0] 

## exercise 6

'''
Given the string "amazing", create a variable called answer, which is a list containing all the letters from "amazing" but not the vowels (a, e, i, o, and u).  
The answer should look like: ['m', 'z', 'n', 'g'].
Use a list comprehension!
'''
answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]