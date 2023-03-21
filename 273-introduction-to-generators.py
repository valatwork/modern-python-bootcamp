'''
Generators are iterators
Generators can be created with generator functions
Generator functions use the yield keyword
Generators can be created with generator expressions


Functions                                   Generator Functions

uses return	                                uses yield
returns once	                            can yield multiple times
When invoked, returns the return value	    When invoked, returns a generator


Exhausting a Generator

Calling next on a generator with nothing left to yield will throw a StopIteration error
When we loop over a generator, the loop will stop before the StopIteration error gets thrown

''''

## example 1

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

count_up_to(5) # <generator object count_up_to at 0x0000015C651D9A10>
counter = count_up_to(5)
counter # <generator object count_up_to at 0x0000015C651DB220>
# counter() TypeError: 'generator' object is not callable
next(counter) # 1

## exercise 1

'''
Write a function called week, which returns a generator that yields each day of the week, starting with Monday and ending with Sunday.  
After Sunday, the generator is exhausted.  
It does not start over.

'''
        
def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day

## exercise 2

# Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on.

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"