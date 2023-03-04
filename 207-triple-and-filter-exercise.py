# Write a function called triple_and_filter. 
# This function should accept a list of numbers, filter out every number that is not divisible by 4, and return a new list where every remaining number is tripled.

'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))
