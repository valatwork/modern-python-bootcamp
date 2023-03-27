## example with phone numbers

import re
# Returns first instance of phone number pattern:
def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

# Returns all instances of phone number pattern in a list
def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

# One way of checking if entire string is valid phone number:
# def is_valid_phone(input):
# 	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
# 	match = phone_regex.search(input)
# 	if match:
# 		return True
# 	return False

# Another way of doing the same thing, using the fullmatch method
def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

# Calling our functions a bunch of times...

print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897622"))
print(extract_phone("432 567-8976 asdjhasd "))
print(extract_phone("432 567-8976"))

print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(extract_all_phones("my number is 432 56"))

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))


## exercise 1 time validating

'''
Write a function called is_valid_time  that accepts a single string argument.  
It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.  
Note that times can start with a single number (2:30) or two (11:18).  

is_valid_time("10:45")       #True
is_valid_time("1:23")        #True
is_valid_time("10.45")       #False
is_valid_time("1999")        #False
is_valid_time("145:23")      #False
In order to return True, the string should ONLY contain the time, and no other characters

is_valid_time("it is 12:15") #False
is_valid_time("12:15")       #True
Don't worry about impossible times like 88:76, just focus on the formatting!

is_valid_time("34:55") #True
'''

import re 
 
def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False

## exercise 2 parsing date

'''
Define a function called parse_date  that accepts a single string.  
Your code should check to see if the string matches a date format.  
We're going to use the DMY format of "dd/mm/yyyy", but it should also work with "dd.mm.yyyy" and "dd,mm,yyyy". 
If you are American, note that Day if before Month!  However, rather than simply returning True or False if the string matches...
you should instead return a dictionary containing the three parts of the date with the keys "d" , "m" , and "y"  like so:

parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}
 Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None

parse_date("12,04,2003")  #{'d': '12', 'm': '04', 'y': '2003'}
parse_date("12.11.2003")  #{'d': '12', 'm': '11', 'y': '2003'}
parse_date("12.11.200312") #None

'''

import re
 
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None