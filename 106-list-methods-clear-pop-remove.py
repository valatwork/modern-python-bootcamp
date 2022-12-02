# clear

first_list = [1, 2, 3, 4]

first_list.clear() # the empty parenthesis are needed

print(first_list) # []

items = ["socks", "mug", "tea pot", "cat food"]
items.clear()

# pop

# Remove the item at the given position in the list, and return it.
# If no index is specified, removes & returns last item in the list.  

first_list = [1, 2, 3, 4]

first_list.pop() # 4

first_list.pop(1) # 2

items = ["socks", "mug", "tea pot", "cat food"]
items.pop() # will remove the last item on the list by default
items.pop(1) # will remove the specified item

# remove

# Remove the first item from the list whose value is x. 
# Throws a ValueError if the item is not found.
# will not return the value

first_list = [1, 2, 3, 4, 4, 4]

first_list.remove(2)

print(first_list) # [1, 3, 4, 4, 4]

first_list.remove(4) # it will only remove the first value

print(first_list) # [1, 3, 4, 4]

# del

# deletes a value from the list

first_list = [1, 2, 3, 4]

del first_list[3]

print(first_list) # [1, 2, 3]

del first_list[1]

print(first_list) # [1, 3]
