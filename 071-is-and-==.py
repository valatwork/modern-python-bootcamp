# In python, "==" and "is" are very similar comparators, however they are not the same
# "is" is only truthy if the variables reference the same item in memory

a = 1
a == 1  # True
a is 1  # True
a = [1, 2, 3]  # a list of numbers
b = [1, 2, 3]
a == b  # True
a is b  # False
c = b
b is c  # True

x = 1
x == 1 # True
x is 1 # True

a = [1, 2, 3]
b = [1, 2, 3]
a == b # True because the same value
a is b # False because they do not occupy the same memory space

c = b
b is c # True

clone = a
a is clone # True
