# A list is a collection of items

# first method

tasks = ["Install Python", "Learn Python", "Take a break"]

# second method

first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"

tasks = [first_task, second_task, third_task]

# thid method: converting a range into a list

tasks = list(range(1, 4))


# len will return the number of items in the list

tasks = ["Install Python", "Learn Python", "Take a break"]

len(tasks) # 3

## exercise

'''
It's time to create your own lists.  Define 2 separate lists: 

First, define a list called my_stuff .  It must be be at least 4 elements long.  
The data is completely up to you, but it must contain at least 1 string and 1 float. 
Next, define a list called nums . It should be a list containing all the numbers between 1 and 99 (including 99). 
Don't type this out manually! Use what we learned at the end of the previous video!
'''

# Define my_stuff 
my_stuff = ["keyboard", "keycaps", "mouse", 99.99]
# Define nums 
nums = list(range(1,100))
