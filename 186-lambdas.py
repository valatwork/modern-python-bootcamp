# normal functions have names

def first_function():
    return 'Hello!'

first_function() # 'Hello!'

first_function.__name__ # first_function'

# but lambdas are anonymous functions
# lambas can only be on a single line

first_lambda = lambda x: x + 5

first_lambda(10) # 15

first_lambda.__name__ # '<lambda>'

# Lambda Syntax
# lambda parameters : body of function

add_values = lambda x, y: x + y

multiply_values = lambda x, y: x + y

add_values(10, 20) # 30

multiply_values(10, 20) # 200

# normally used to pass a function into another function that will be used only once

# exercise

# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube .

# cube(2)  # 8

# cube(3)  # 27

# cube(8)  # 512

# This challenge has tests ensuring that cube  is a lambda rather than a function, so don't cheat and make it a plain old function :) 

cube = lambda num: num ** 3
