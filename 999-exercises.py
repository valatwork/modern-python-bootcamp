## exercise 108

'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!
def reverse_string(string):
    # implement your function here
    return string[::-1]

# different solution

def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s

## exercise 109

'''
Write a function called list_check, which accepts a list and returns True if each value in the list is a list.
Otherwise the function should return False.

list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

# def list_check(lst):
#     for item in lst:
#         if not isinstance(item, list):
#             return False
#     return True

# solution

def list_check(vals):
    return all(type(l) == list for l in vals)

## exercise 110

'''
Write a function called remove_every_other that accepts a list and returns a new list with every second value removed.

remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''
# my solution

def remove_every_other(lst):
    return lst[::2]

# given solution

def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]
            

## exercise 111

'''
Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function.

sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(lst, num):
    seen = set()
    for x in lst:
        target = num - x
        if target in seen:
            return [target, x]
        seen.add(x)
    return []

## exercise 112

'''
Write a function called vowel_count that accepts a string and returns a dictionary 
with the keys as the vowels and values as the count of times that vowel appears in the string.

vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

# def vowel_count(string):
#     vowels = 'aeiou'
#     counts = {char.lower(): string.lower().count(char.lower()) for char in string if char.lower() in vowels}
#     return counts

def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


# def vowel_count(string):
#     vowels = 'aeiou'
#     return {vowel: string.count(vowel) for vowel in string}

    
    
    # counts = {}
    # for char in string:
    #     if char.lower() in vowels:
    #         counts[char.lower] = counts.get(char.lower(), 0) + 1
    # return counts
    
## exercise 113

'''
Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string capitalized.
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

## exercise 114

'''
Write a function called find_factors which accepts a number and returns a list of all of the numbers which are is divisible by starting from 1 and going up to the number.

find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''

def find_factors(num):
    factors = []
    i = 1
    while(i <= num):
        if (num % i == 0):
            factors.append(i)
        i += 1
    return factors

## exercise 115

'''
Write a function called includes which accepts a collection, a value, and an optional starting index. 
The function should return True if the value exists in the collection when we search starting from the starting index. Otherwise, it should return False.

The collection can be a string, a list, or a dictionary. If the collection is a string or array, the third parameter is a starting index for where to search from. 
If the collection is a dictionary, the function searches for the value among values in the dictionary; since objects have no sort order, the third parameter is ignored.

includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]

## exercise 116

'''
Write a function called repeat, which accepts a string and a number and returns a new string with the string passed to the function repeated the number amount of times. 
Do not use the built in repeat method!

repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr

## exercise 117

'''
Write a function called truncate that will shorten a string to a specified length, and add "..." to the end.  
Given a string and a number n, truncate the string to a shorter string containing at most n characters.
For example, truncate("long string", 5) should return a 5 character truncated version of "long string".  
If the string gets truncated, the truncated return string should have a "..." at the end. 

Because of this, the smallest number passed in as a second argument should be 3. 
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate():
    pass

def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string
 
    return string[:n - 3] + "..."

## exercise 118

'''
Write a function called two_list_dictionary which accepts two lists of varying lengths.The first list consists of keys and the second one consists of values. 
Your function should return a dictionary created from the keys and values. 
If there are not enough values, the remaining keys should have a value of null. 
If there not enough keys, just ignore the remaining values.

two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(keys, values):
    collection = {}
 
    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None
 
    return collection

## exercise 119

'''
Write a function called range_in_list which accepts a list and start and end indices, and returns the sum of the values between (and including) the start and end index.
If a start parameter is not passed in, it should default to zero. If an end parameter is not passed in, it should default to the last value in the list. 
Also, if the end argument is too large, the sum should still go through the end of the list.

range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''

def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])

## exercise 120

'''
Write a function called same_frequency which accepts two numbers and returns True if they contain the same frequency of digits. 
Otherwise, it returns False.

same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True

## exercise 121

'''
Write a function called nth, which accepts a list and a number and returns the element at whatever index is the number in the list.
If the number is negative, the nth element from the end is returned.

You can assume that number will always be between the negative value of the list length, and the list length minus 1.

nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]

## exercise 122

'''
Write a function called find_the_duplicate which accepts an array of numbers containing a single duplicate. 
The function returns the number which is a duplicate or None if there are no duplicates.

find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)

## exercise 123

'''
Write a function called sum_up_diagonals which accepts an NxN list of lists and sums the two main diagonals in the array: 
the one from the upper left to the lower right, and the one from the upper right to the lower left.

EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''

def sum_up_diagonals(arr):
    total = 0
    
    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total

## exercise 124

'''
Write a function called min_max_key_in_dictionary which returns a list with the lowest key in the dictionary and the highest key in the dictionary. 
You can assume that the dictionary will have keys that are numbers.

min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]

## exercise 125

'''
Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed by a larger number across the entire list. 

find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count;

## exercise 126

'''
Write a function called two_oldest_ages. The function should take a list of numbers as its argument and return the two highest numbers within the list. 
The returned value should be a list in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order.

two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(ages):
    return sorted(ages)[-2:]


'''
Write a function called is_odd_string which returns true if sum of each character's position in the alphabet is odd. For example, "a" is in the first position, "b" is in the second position, and so on. 
If the sum is even, return false.  
INDEXING STARTS AT 1.  A is position 1, NOT POSITION 0.

is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1

## exercise 128

'''
Write a function called valid_parentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. 
Valid_parentheses should return true if the string is valid, and false if it's invalid.

valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(parens):
    count = 0
    i = 0
    while i < len(parens):
        if (parens[i] == '('):
            count += 1
        if (parens[i] == ')'):
            count -= 1
        if (count < 0):
            return False
        i += 1
    return count == 0

## exercise 129

'''
Write a function called reverse_vowels. This function should reverse the vowels in a string. 
Any characters which are not vowels should remain in their original position. You should not consider "y" to be a vowel.

reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)


## exercise 130

'''
Write a function called three_odd_numbers, which accepts a list of numbers and returns True  if any three consecutive numbers sum to an odd number.

three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(arr):
    i = 0
    while(i < (len(arr) -2)):
        total = 0
        j = i
        while(j <= i+2):
            total += arr[j]
            j+=1
            
        if (j-i) % 3 == 0 and total % 2 != 0:
            return True
            
        i+= 1
    return False

## exercise 131

'''
Write a function called mode. 
This function accepts a list of numbers and returns the most frequent number in the list of numbers. 
You can assume that the mode will be unique.

mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]

## exercise 132

'''
Create a function running_average that returns a function. 
When the function returned is passed a value, the function returns the current average of all previous function calls. 
You will have to use closure to solve this. You should round all answers to the 2nd decimal place.

rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''

def running_average():
    running_average.accumulator = 0
    running_average.size = 0
  
    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size
    
    return inner

## exercise 133

'''
Write a function called letter_counter which accepts a string and returns a function. 
When the inner function is invoked it should accept a parameter which is a letter, and the inner function should return the number of times that letter appears. 
This inner function should be case insensitive.


counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(s):
    letter_counter.val = s
    def inner(char):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
    return inner

## exercise 134

'''
Write a function called once. This function accepts a function and returns a new function that can only be invoked once. 
If the function is invoked more than once, it should return None. 
Hint you will need to define a new function inside of your once function and return that function. 
You can add properties to your inner function to see if it has run already.

def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''

def once(fn):
    fn.is_called = False
    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner

## exercise 135

'''
Write a function called next_prime, which returns a generator that will yield an unlimited number of primes, starting from the first prime (2).

Recall that a prime number is any whole number that has exactly two divisors: one and the number itself. The first few primes are 2, 3, 5, 7, 11, ... .

primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''

def next_prime():
    num = 2
    all_primes = set()
    while True:
        for prime in all_primes:
            if num % prime == 0:
                break
        else:
            all_primes.add(num)
            yield num
        num += num % 2 + 1
