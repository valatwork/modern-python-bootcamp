## max
# Return the largest item in an iterable or the largest of two or more arguments.

# max (strings, dicts with same keys)

max([3,4,1,2]) # 4
max((1,2,3,4)) # 4
max('awesome') # 'w'
max({1:'a', 3:'c', 2:'b'}) # 3

## min

# Return the smallest item in an iterable or the smallest of two or more arguments.

# min (strings, dicts with same keys)

min([3,4,1,2]) # 1
min((1,2,3,4)) # 1
min('awesome') # 'a'
min({1:'a', 3:'c', 2:'b'}) # 1

## example

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA

## exercise

# Write a function called extremes  which accepts an iterable. It should return a tuple containing the minimum and maximum elements.  For example:

# extremes([1,2,3,4,5])  # (1, 5)

# extremes((99,25,30,-7))  # (-7, 99)

# extremes("alcatraz")  #( 'a', 'z')

# REMEMBER, RETURN A TUPLE!!!

def extremes(nums):
    return(min(nums), max(nums))