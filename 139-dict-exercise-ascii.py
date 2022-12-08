# This is a bit different. Every character has an ASCII code (basically, a number that represents it).  
# Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code.  
# For example:
# chr(65)  will return  'A'
# chr(66)  will return  'B'
# All the way up to:
# chr(90)  will return  'Z'

# Your task is to create dictionary that maps ASCII keys to their corresponding letters.  
# Use a dictionary comprehension and chr() . Save the result to the answer variable. 
# You only need to care about capital letters (65-90).


answer = {count: chr(count) for count in range(65,91)} 

# my initial attempt was to use chr() as a range, but: 
# TypeError: chr() takes exactly one argument (2 given)
# chr() only works with int, hence the count variable