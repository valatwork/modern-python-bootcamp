## using modules

import random

# importing part of a module

''' 
The from keyword lets you import parts of a module
Handy rule of thumb: only import what you need!
If you still want to import everything, you can also use the from MODULE import * pattern

'''

from random import choice as pick, randint as magic_number_chooser

'''
Different ways to import

import random
import random as omg_so_random
from random import *
from random import choice, shuffle
from random import choice as gimme_one, shuffle as mix_up_fruits

'''

# example 1

print(pick(["apple", "banana", "cherry", "durian"]))
print(magic_number_chooser(1,100))

# example 2

import random

random.choice(["apple", "banana", "cherry", "durian"])
random.shuffle(["apple", "banana", "cherry", "durian"])

# example 3

import random as omg_so_random

omg_so_random.choice(["apple", "banana", "cherry", "durian"])
omg_so_random.shuffle(["apple", "banana", "cherry", "durian"])

# example 4

import random as r

r.choice(["apple", "banana", "cherry", "durian"])
r.shuffle(["apple", "banana", "cherry", "durian"])