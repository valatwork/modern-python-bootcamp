'''
Iterator - an object that can be iterated upon. An object which returns data, one element at a time when next() is called on it

Iterable -  An object which will return an Iterator when iter() is called on it.

"HELLO" is an iterable, but it is not an iterator.

iter("HELLO") returns an iterator

'''

# example 1

name = "Oprah"
# next(name) # TypeError: 'str' object is not an iterator

iter(name) # <str_iterator at 0x2b2f6aa77c0>
it = iter(name) # <str_iterator at 0x2b2f6aa77c8>

'''
When next() is called on an iterator, the iterator returns the next item. 
It keeps doing so until it raises a StopIteration error.

'''
next(it) # 'O'
next(it) # 'p'
next(it) # 'r'
next(it) # 'a'
next(it) # 'h'
next(it) # StopIteration

# example 2

nums = [1,2,3,4,5]
# next(nums) # TypeError: 'list' object is not an iterator
iter(nums)
nu = iter(nums)
nu # <list_iterator at 0x2117fbb62c0>