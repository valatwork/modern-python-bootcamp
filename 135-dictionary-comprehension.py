# the syntax

# { ____:____ for ___ in ____}

# - iterates over keys by default
# - it iterate over keys and values using .items()

## example 1

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}

## example 2

{num: num**2 for num in [1,2,3,4,5]} # creating a dictionary starting from the list [1,2,3,4,5] and the key is num

## example 3

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} # loops through the string and assigns key to value in order, starting from 0
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}

## example 4

instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}

# conditional logic with dictionaries

## example 1

num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd") for num in num_list }

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

## example 1.1

{ num:("even" if num % 2 == 0 else "odd") for num in range(1,100) } # same as above but with a range

## example 2
instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {(k.upper() if k is 'color' else k):v.upper() for k,v in instructor.items()} # {'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}