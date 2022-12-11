## exercise 1

# Write a function called product that accepts two parameters and returns the product of the two parameters (multiply them together)
def product(a,b):
    return a*b

## exercise 2

# Write a function called return_day. this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). 
# If the number is less than 1 or greater than 7, the function should return None
# Hint: store the days of the week in a list (or dict using numbers as keys).

# '''
# return_day(1) # "Sunday"
# return_day(2) # "Monday"
# return_day(3) # "Tuesday"
# return_day(4) # "Wednesday"
# return_day(5) # "Thursday"
# return_day(6) # "Friday"
# return_day(7) # "Saturday"
# return_day(41) # None
# '''

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num > 0 and num <= len(days):
        return days[num-1]
    return None
    
# alternative solution

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None
    
## exercise 3

# Write a function called last_element. This function takes in one parameter (a list) and returns the last value in the list. 
# It should return None if the list is empty.

def last_element(list):
    if list:
        return l[-1]
    return None
print(last_element([]))

## exercise 4

# Write a function called number_compare. This function takes in two parameters (both numbers). 
# If the first is greater than the second, this function returns "First is greater" 
# If the second number is greater than the first, the function returns "Second is greater" 
# Otherwise the function returns "Numbers are equal"

# '''
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,0) # "First is greater"
# number_compare(2,4) # "Second is greater"
# '''

def number_compare(num1,num2):
    if num1 < num2:
        return 'Second is greater'
    elif num1 > num2:
        return 'First is greater'
    return 'Numbers are equal'

# Write a function called single_letter_count. 
# This function takes in two parameters (two strings). 
# The first parameter should be a word and the second should be a letter. 
# The function returns the number of times that letter appears in the word. 
# The function should be case insensitive (does not matter if the input is lowercase or uppercase). 
# If the letter is not found in the word, the function should return 0.  
# Hint: take advantage of count() method

# '''
# single_letter_count("Hello World", "h") # 1
# single_letter_count("Hello World", "z") # 0
# single_letter_count("HelLo World", "l") # 3
# '''

#define single_letter_count below:

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())


## exercise 5

# Write a function called multiple_letter_count. 
# This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.  
# Hint: use a dictionary comprehension and count(). 

# Here's how it should work:

# multiple_letter_count("awesome")   # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

## exercise 6

# Write a function called list_manipulation. This function should take in four parameters (a list, command, location and value).

# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
    
## exercise 7

# Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. 
# This function should take in one parameter and returns True or False depending on whether it is a palindrome. 
# As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.

# '''
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True
# '''

def is_palindrome(string):
    return string == string[::-1]

# advanced solution that ignores whitespace

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

## exercise 8

# Write a function called frequency. 
# This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.

# '''
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1
# '''

def frequency(collection, searchTerm):
    return collection.count(searchTerm)

## exercise 9

# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.

# '''
# multiply_even_numbers([2,3,4,5,6]) # 48
# '''

def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

## exercise 10

# Write a function called capitalize. This function accepts a string and returns the same string with the first letter capitalized.  
# You may want to use slices to help you out.

# capitalize("jamaica") # "Jamaica"
# capitalize("chicken") # "Chicken"

# '''
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"
# '''

def capitalize(string):
    return string[:1].upper() + string[1:]

## exercise 11

# Write a function called compact. 
# This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.

# compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]

# '''
# compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
# '''

def compact(l):
    return [val for val in l if val]

# solution withou list comprehension

def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals

## exercise 12

# Write a function called intersection. 
# This function should accept two lists and return a list with the values that are in both input lists.

# intersection([1,2,3], [2,3,4])    #[2,3]
# intersection(['a','b','z'], ['x','y','z']) .  # ['z']

# flesh out intersection pleaseeeee
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

# list comprehension solution

def intersection(l1, l2):
    return [val for val in l1 if val in l2]

# sets solution

def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

## exercise 13

# Write a function called partition. This function accepts a list and a callback function (which you can assume returns True  or False  ). 

# The function should iterate over each element in the list and invoke the callback function at each iteration. 

# If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
# If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
# When it's finished, partition should return both lists inside of one larger list, like so:

# [truthy_list, falsy_list] 

# '''
# def isEven(num):
#     return num % 2 == 0

# partition([1,2,3,4], isEven) # [[2,4],[1,3]]
# '''

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

# list comprehension solution

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

# another solution

def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]