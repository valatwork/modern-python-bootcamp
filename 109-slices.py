# slicing
# Make new lists using slices of the old list!

# some_list[start:end:step]

# start: what index to start slicing from
first_list = [1, 2, 3, 4]
first_list[1:] # [2, 3, 4]
first_list[3:] # [4]

# If you enter a negative number, it will start the slice that many back from the end

first_list[-1:] # [4]
first_list[-3:] # [2, 3, 4]

# Second Parameter for Slice: end
# The index to copy up to (exclusive counting).

first_list = [1, 2, 3, 4]
first_list[:2] # [1, 2]
first_list[:4] # [1, 2, 3, 4]
first_list[1:3] # [2, 3]

# With negative numbers, how many items to exclude from the end (i.e. indexing by counting backwards)

first_list[:-1] # [1, 2, 3]
first_list[1:-1] # [2, 3]

# Third Parameter for Slice: step
# "step" in Python is basically the number to count at a time 
# same as step with range!
# for example, a step of 2 counts every other number (1, 3, 5)

first_list = [1, 2, 3, 4, 5, 6]
first_list[1::2] # [2, 4, 6]
first_list[::2] # [1, 3, 5]

# with negative numbers, reverse the order 

first_list[1::-1] # [2, 1]
first_list[:1:-1] # [6, 5, 4, 3]
first_list[2::-1] # [3, 2, 1]

# reversing lists/strings

string = "This is fun!"

string[::-1]

# modifying portions of lists

numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a','b','c']

print(a) # [1, 'a', 'b', 'c', 4, 5]


##################

colors = ["red", "orange", "orange", "yellow", "green", "blue", "indigo", "violet"]

# start
colors[2]       # "yellow"
colors[2:]      # ["yellow", "green", "blue", "indigo", "violet"]
colors[0:]      # it is a different object ["red", "orange", "orange", "yellow", "green", "blue", "indigo", "violet"]
colors[-2:]     # ["indigo", "violet"]

# end
colors[:5]      # ["yellow", "green", "blue"]
colors[2:4]     # ["yellow", "green"]

#step
colors[::2]     # ["red", "yellow", "violet"]
colors[::-1]    # ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
colors[0]       # "red"
colors[5][::-1] # "ogidni"