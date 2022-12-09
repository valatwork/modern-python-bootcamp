# Why use Keyword Arguments?
# You may not see the value now, but it's useful when passing a dictionary to a function and unpacking it's values - we'll see that later!
# A little more flexibility


# order does not matter

def full_name(first, last):
    return "Your name is {first} {last}"

full_name(first='Colt', last='Steele') # Your name is Colt Steele

full_name(last='Steele', first='Colt') # Your name is Colt Steele

## example 2

def exponent(num, power=2):
    return num ** power

print(exponent(power=3, num=4))
#64

print(exponent(power=4, num=3))
#64

# Different from Default Params
# When you define a function and use an = you are setting a default parameter
# When you invoke a function and use an = you are making a keyword argument

def full_name(first="Colt", last="Steele"):
    return "Your name is {first} {last}"

full_name() # Your name is Colt Steele

full_name(last='Enthusiast', first='Python') # Your name is Python Enthusiast