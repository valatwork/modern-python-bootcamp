# Using * as an Argument:
# Argument Unpacking
# We can use * as an argument to a function to "unpack" values

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
        print(total)
        
sum_all_values(1,30,2,5,6)

# trying with a list

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
        print(total)
        
nums = [1,2,3,4,5,6]
sum_all_values(nums)
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# trying with a tuple

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
        print(total)
        
nums = (1,2,3,4,5,6)
sum_all_values(nums)
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'


def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    return sum(args)

# sum_all_values([1, 2, 3, 4]) # nope...
# sum_all_values((1, 2, 3, 4)) # this does not work either...

# correct code

sum_all_values(*[1, 2, 3, 4]) # 10
sum_all_values(*(1, 2, 3, 4)) # 10