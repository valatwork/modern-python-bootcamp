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
