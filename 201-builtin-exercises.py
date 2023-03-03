## exercise 1: greatest magnitude

# Write a function max_magnitude  that accepts a single list full of numbers. 
# It should return the magnitude of the number with the largest magnitude (the number that is furthest away from zero).

# max_magnitude([300, 20, -900])   #900

# max_magnitude([10, 11, 12])   #12

# max_magnitude([-5, -1, -89])   #89

# Hint: use max and abs!

def max_magnitude(nums):
    return max(abs(num) for num in nums)

## exercise 2: sum even values

# Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. 
# If there are no numbers divisible by 2, the function should return 0.  
# To be clear, it accepts all the numbers as individual arguments!

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values


# Sum Even Values Solution
# I define a function called sum_even_values  which accepts any number of arguments, thanks to *args 
# I grab the even numbers using the generator expression (arg for arg in args if arg % 2 == 0)  (could also use a list comp)
# I pass the even numbers I extracted into sum()  and return the value
# The default start value of sum()  is 0, so I don't have to do anything special to get it to return 0 if there are no even numbers!


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

## exercise 3: sum floats

# Write a function called sum_floats. This function should accept a variable number of arguments. 
# The function should return the sum of all the parameters that are floats. 
# If there are no floats the function should return 0

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

# I started by defining sum_floats , which accepts any number of arguments using *args 
# Much like the previous exercise, I use a generator expression to extract the values in args where type()  is float.
# I pass those values in to sum  and return the result


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)