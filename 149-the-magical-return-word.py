# return
# Exits the function
# Outputs whatever value is placed after the return keyword, could be a tuple
# Pops the function off of the call stack (the 'to do list' for all the tasks that python has to do in executing the code)
# return is used to return the result of a function when called

def print_square_of_7():
    print(7**2)
print_square_of_7()
# 49

# example 1

def square_of_7():
    7**2
result = square_of_7()
print(result)
# None

def square_of_7():
    return 7**2
result = square_of_7()
print(result)
# 49

# example 2

def say_hi():
    'Hello!'

say_hi() # None


def say_hi():
    print('Hello!')

result = say_hi() 

print(result) # None


def say_hi():
    return 'Hi!'

greeting = say_hi()

print(greeting) # 'Hi!'

# example 3

def square_of_7():
    print("BEFORE the return")
    return 7**2
    print("AFTER the return") # no output
result = square_of_7()
print(result)

### exercise 1

# Generating evens using a list comprehension:

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

# Generating evens using a loop:

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result

### exercise 2

# Using string concatenation:

def yell(word):
    return word.upper() + "!"

# Using the string format() method:

def yell(word):
    return "{}!".format(word.upper())

# Using an f-string. My personal favorite, but only works in python 3.6 or later.  Udemy exercises don't support it currently :(

def yell(word):
    return f"{word.upper()}!"

### execise 3

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# other solution

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"
