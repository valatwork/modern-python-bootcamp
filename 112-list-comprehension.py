# List Comprehension vs Looping

## loop
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers) # [2, 4, 6, 8, 10]

## list 

numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers) # [2, 4, 6, 8, 10]

## example 1

name = 'colt'

[char.upper() for char in name] # ['C', 'O', 'L', 'T']

## example 2

friends = ['ashley', 'matt', 'michael']

[friend[0].upper() + friend[1:] for friend in friends] # ['Ashley', 'Matt', 'Michael']

## example 3

[num*10 for num in range(1,6)] # [10, 20, 30, 40, 50]

## example 4

[bool(val) for val in [0, [], '']] # [False, False, False]

## example 5

numbers = [1, 2, 3, 4, 5]

string_list = [str(num) for num in numbers]

print(string_list) # ['1', '2', '3', '4', '5']

## example 6

colors = ["red", "orange", "orange", "yellow", "green", "blue", "indigo", "violet"]

[color.upper() for color in colors]

nums = [1, 2, 3]
[str(num)+ " HELLO" for num in nums]