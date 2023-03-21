# for num in [1,2,3] # iter is called on the list
# for char in "hi there" # iter is called on the string

## example 1

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:    
            print(next(iterator))
        except StopIteration:
            print("END OF ITERATOR")
            break

my_for("hello")

# h
# e
# l
# l
# o
# END OF ITERATOR

## example 2

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:    
            print(next(iterator))
        except StopIteration:
            print("END OF ITERATOR")
            break

my_for([1,2,3,4])

# 1
# 2
# 3
# 4
# END OF ITERATOR

## example continued

def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:    
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

# my_for([1,2,3,4], print)

my_for("lol", print)
my_for([1,2,3,4,5], square)

# l
# o
# l
# 1
# 4
# 9
# 16
# 25