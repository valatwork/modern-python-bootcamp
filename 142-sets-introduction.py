# Sets are more lightweight than lists and dicts
# Sets are like formal mathematical sets.
# Sets are a collection of data that do not have duplicate values
# Elements in sets aren't ordered.
# You cannot access items in a set by index (as they are not ordered)
# Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates

# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s
# True

8 in s
# False

s = {1, 'a', 4, 5, 'b' 23.3334} # this is a valid set

# accessing data

numbers = {1,2,3,4}

for number in numbers:
    print(number)

# 1
# 2
# 3
# 4

s = {1, 'a', 4, 5, 'b' 23.3334}
for thing in s:
    print(thing)
    
# 1
# 4
# 5
# 23.3334
# a
# b

cities = ['Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago', 'Los Angeles', 'Shanghai', 'Oslo', 'Boulder', 'San Francisco', 'Oslo', 'Tokyo']
# print(set(cities))
# {'Boulder', 'Los Angeles', 'Oslo', 'Santiago', 'Kyoto', 'San Francisco', 'Tokyo', 'Florence', 'Shanghai'}
# print(list(set(cities)))
# ['Boulder', 'Los Angeles', 'Oslo', 'Santiago', 'Kyoto', 'San Francisco', 'Tokyo', 'Florence', 'Shanghai']
print(len(set(cities)))
# 9