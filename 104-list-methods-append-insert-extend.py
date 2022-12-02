# append - add one (and only one!) item at the end of the list

first_list = [1, 2, 3, 4]

first_list.append(5)

print(first_list) # [1, 2, 3, 4, 5]


# extend - add multiple items to the end of the list

first_list = [1, 2, 3, 4]

first_list.append(5, 6, 7, 8) # does not work!

first_list.append([5, 6, 7, 8]) # this will be added as a single item

print(first_list) # [1, 2, 3, 4,  [5, 6, 7, 8]]

correct_list = [1, 2, 3, 4]

correct_list.extend([5, 6, 7, 8])

print(correct_list) # [1, 2, 3, 4, 5, 6, 7, 8]


# insert - insert an item at a given position

first_list = [1, 2, 3, 4]

first_list.insert(2, 'Hi!') 

print(first_list) # [1, 2, 'Hi!', 3, 4]

first_list.insert(-1, 'The end!') 

print(first_list) # [1, 2, 'Hi!', 3, 'The end!', 4]
