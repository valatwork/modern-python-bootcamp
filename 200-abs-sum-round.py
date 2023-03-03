## abs

# Return the absolute value of a number. The argument may be an integer or a floating point number.

abs(-5) # 5
abs(5)  # 5

## sum

# Takes an iterable and an optional start.
# Returns the sum of start and the items of an iterable from left to right and returns the total.
# start defaults to 0

sum([1,2,3,4]) # 10

sum([1,2,3,4], -10) # 0

## round

# Return number rounded to ndigits precision after the decimal point. 
# If ndigits is omitted or is None, it returns the nearest integer to its input.

round(10.2) # 10
round(1.212121, 2) # 1.21