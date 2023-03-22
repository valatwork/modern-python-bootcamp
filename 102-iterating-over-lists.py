# Accessing All Values in a List

# FOR loop

## example 1

numbers = [1,2,3,4]

for number in numbers:
    print(number)

# 1
# 2
# 3
# 4

## example 2

colors = ["purple", "teal", "magenta"]

for color in colors:
    print(color)

## example 3

numbers = [4,6,2,9,7,10]
for num in numbers:
    print(num * num)


# WHILE loop

## example 1

numbers = [1, 2, 3, 4]
i = 0 # index, starting from the first value
while i < len(numbers):
    print(numbers[i])
    i += 1 # adds 1 to the index value

## example 2

colors = ["purple", "teal", "magenta", "crimson", "emerald"]

index = 0
while index < len(colors): # this is necessary to prevent an infinite loop
   print(colors[index]) # if this is not incremented, it will just print purple over and over
   index += 1

## example 3

while index < len(colors): 
    print(f"{index}: {colors[index]}") # this will print the position of each item within the list
    index += 1


## exercise

'''
I've given you a list called sounds .  It looks like this:

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"] 

Write code that loops over the list and adds all the strings together to form one large combined string (don't add any spaces between them) 
The combined string should be in all UPPERCASE as well 
Save the result in a variable called result  
'''

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()