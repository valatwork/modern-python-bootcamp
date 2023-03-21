'''
Write a function called delay which accepts a time and returns an inner function that accepts a function. 
When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it. 
Before starting the timer, delay will also print a message informing the user that there will be a delay before the decorated function gets run.
(Hint: take a look at the sleep function from the built-in time module if you want to pause code execution for a certain amount of time.)
'''

from functools import wraps
from time import sleep
 
def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner