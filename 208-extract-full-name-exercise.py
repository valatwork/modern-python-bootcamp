# Write a function called extract_full_name. 
# This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))