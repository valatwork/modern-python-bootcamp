# loop

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []

# for num in numbers:
#     doubled_number = num * 2
#     doubled_numbers.append(doubled_number)

# print(doubled_numbers) # [2, 4, 6, 8, 10]

#list 

numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers) # [2, 4, 6, 8, 10]


name = 'colt'

[char.upper() for char in name] # ['C', 'O', 'L', 'T']

friends = ['ashley', 'matt', 'michael']

[friend[0].upper() + friend[1:] for friend in friends] # ['Ashley', 'Matt', 'Michael']

[num*10 for num in range(1,6)] # [10, 20, 30, 40, 50]

[bool(val) for val in [0, [], '']] # [False, False, False]

numbers = [1, 2, 3, 4, 5]

string_list = [str(num) for num in numbers]

print(string_list) # ['1', '2', '3', '4', '5']


colors = ["red", "orange", "orange", "yellow", "green", "blue", "indigo", "violet"]

[color.upper() for color in colors]

nums = [1, 2, 3]
[str(num)+ " HELLO" for num in nums]