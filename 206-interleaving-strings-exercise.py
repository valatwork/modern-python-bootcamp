'''
# Write a function interleave  that accepts two strings.  
# It should return a new string containing the 2 strings interwoven or zipped together. For example:

# interleave('hi','ha')    # 'hhia'

# interleave('aaa', 'zzz')  # 'azazaz'

# interleave('lzr','iad') #  'lizard'

# 1. suppose we call interleave('hi', 'no')  
# 2. zip  the two strings together, giving you a list of tuples (once you convert from the default zip_object) -  [('h','n'), ('i','o')]  
# 3. For each of the tuples in the list, join them together using "".join  resulting in ['hn', 'io']  - Easiest if you use a list comp.  You need to join EACH tuple.
# 4. Finally, join the items in the list together using "".join  again resulting in 'hnio'  

'''

def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

'''
# Here's a detailed walkthrough.  I know it can be overwhelming, but try to step through one piece at a time if you get stuck.

# * I start by defining interleave , which accepts 2 strings: str1, and str2
# * To make this easier, let's use an example. Let's say that I call interleave('hi', 'no') 
# * Focus on the innermost bit first. I zip the two strings together, which returns a list of tuples like: [('h','n'), ('i','o')] 
# * To get it back into a string, I need to:
#     * First join the individual tuples into strings, which is what the first join() does it results in a list of strings: ['hn', 'io'] 
#     * Finally, join all the remaining strings into one large string
#         * it results in 'hnio' 
#     * Return the result!
'''
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))
