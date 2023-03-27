## example

import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())

## exercise

'''
Write a function called parse_bytes  that accepts a single string.  
It should return a list of the binary bytes contained in the string.  
Each byte is just a combination of eight 1's or 0's. For example:

parse_bytes("11010101 101 323")    # ['11010101']

parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']

parse_bytes("asdsa")   # []

Hints: take advantage of \b Not all bytes will have a space before and after, some come at the beginning of a file or at the end.  Use findall!
'''

import re
 
def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results
