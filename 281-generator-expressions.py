'''
You can also create generators from generator expressions
Generator expressions look a lot like list comprehensions
Generator expressions use () instead of []

'''

## example 1

def nums():
    for num in range(1,10):
        yield num

g = nums()
next(g)

# in a single line 

g = (num for num in range(1,10))
g # <generator object <genexpr> at 0x00000270B4BDDA80>

## example 2 (list)

l = [num for num in range(1,10)]
l # [1, 2, 3, 4, 5, 6, 7, 8, 9]

## example 3

sum([num for num in range(1,10)]) # list comprehension
sum(num for num in range(1,10)) # generator expression

## example 3

import time

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(10000000)])) # we turn it into a list first
list_time = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) took: {gen_time}") # sum(n for n in range(10000000)) took: 0.45600223541259766
print(f"sum[n for n in range(10000000)] took: {list_time}") # sum[n for n in range(10000000)] took: 0.6774985790252686

## example 3 continued

import time

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(100000000)])) # we turn it into a list first
list_time = time.time() - list_start_time

print(f"sum(n for n in range(100000000)) took: {gen_time}") # sum(n for n in range(100000000)) took: 4.333998203277588
print(f"sum[n for n in range(100000000)] took: {list_time}") # sum[n for n in range(100000000)] took: 7.362500429153442

## example 4

def sum_of_nums():
    total = 0
    num = 1
    while True:
        total += num
        yield total
        num += 1

s = sum_of_nums() # another generator!

'''
Lazy Evaluation

Also called calculation on demand
Only compute values as needed
Can help improve performance of your code

An Example

Some Number Theory!

A number is called abundant if the sum of all of its proper divisors exceeds the number.

Examples:

12 (1 + 2 + 3 + 4 + 6 > 12)
18 (1 + 2 + 3 + 6 + 9 > 18)
20 (1 + 2 + 4 + 5 + 10 > 20) 

Non-Examples:

4 (1 + 2 < 4)
6 (1 + 2 + 3 = 6)
15 (1 + 3 + 5 < 15)

'''

## Generating Abundant Numbers

def is_abundant(n):
    total = 0
    for d in range(1,n):
        if n % d == 0:
            total += d
    return total > n

is_abundant(12) # True
is_abundant(4) # False

## Lists vs Generatora

# list

def list_first_abundants(n):
    abundant_nums = []
    num = 1
    while len(abundant_nums) < n:
        if is_abundant(num):
            abundant_nums.append(num)
        num += 1
    return abundant_nums

# generator

def gen_first_abundants(n):
    count = 0
    num = 1
    while count < n:
        if is_abundant(num):
            yield num
            count += 1
        num +=1
        
'''
Generators are iterators
Generators can be created with generator functions using the yield keyword
Generators can be created with generator expressions
Generators may or may not have terminating conditions
Generators can provide memory savings
Generators calculate values as they are needed

'''