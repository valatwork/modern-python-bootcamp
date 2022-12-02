# index
# returns the index of the specified value in the list

numbers = [5, 6, 7, 8, 9, 10]

numbers.index(6) # 1
numbers.index(9) # 4

# can specify start and end

numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]

numbers.index(5) # 0 it will specify only the FIRST time it fnds the value
numbers.index(5, 1) # 1 find the index of 5 after the index of 1
numbers.index(5, 2) # 4 find the index of 5 after the index of 2

numbers.index(8, 6, 8) # 6 looking for 8 between the index 6 and 8

# count 

# return the number of times the specified item appears in the list

numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]

numbers.count(2) # 3
numbers.count(21) # 0
numbers.count(3) # 2

# reverse 
# the elements of the list (in-place) - it updates the list and does not create a new one

first_list = [1, 2, 3, 4]

first_list.reverse()

print(first_list) # [4, 3, 2, 1]

# sort
# sort the items of the list (in-place) in ascending order

another_list = [6, 4, 1, 2, 5]

another_list.sort()

print(another_list) # [1, 2, 4, 5, 6]

# join
# technically a String method that takes an iterable argument
# concatenates (combines) a copy of the base string between each item of the iterable
# returns a new string
# can be used to make sentences out of a list of words by joining on a space, for instance:

words = ['Coding', 'Is', 'Fun!']

' '.join(words) # 'Coding is Fun!'

name = ['Mr', "Steele"]

'. '.join(name) # 'Mr. Steele'