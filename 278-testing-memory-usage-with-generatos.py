# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
     nums = []
     a, b = 0, 1
     while len(nums) < max:
         nums.append(b) 
         a, b = b, a+b
     return nums

# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


for n in fib_gen(1000000):
	print(n)
 
 
## exercise 1

'''
Write a function called get_multiples, which accepts a number and a count, and returns a generator that yields the first count multiples of the number. 

The default number should be 1, and the default count should be 10.

'''

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num
        
## exercise 2

'''
Write a function called get_unlimited_multiples, which accepts a number and returns a generator that will yield an unlimited number of multiples of that number.

The default number should be 1.

sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num

