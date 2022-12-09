# looping

names = ('Colt', 'Blue', 'Rusty', 'Lassie')

for name in names:
    print(name)

# Colt
# Blue
# Rusty
# Lassie

i = len(names) -1
while i >= 0:
    print(names[i])
    i -= 1
    
# Lassie
# Rusty
# Blue
# Colt

# count

## Returns the number of times a value appears in a tuple:

x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

# index

## Returns the index at which a value is found in a tuple.

t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned