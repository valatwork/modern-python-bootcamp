# Use """ """
# Essential when writing complex functions

def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"

say_hello.__doc__ # 'A simple function that returns the string hello'

from random import random

random.randint.__doc__