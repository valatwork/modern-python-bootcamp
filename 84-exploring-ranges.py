# range(7) # integers from 0 to 7

# range(1,8) # integers from 1 to 7

# range(1,10,2) # odds from 1 to 10

# range(7,0,-1) # integers from 7 to 1

# r = range(10)
# list(r)

# for num in range(10):
#     print(num)

# for num in range(10,20,2):
#     print(num)

# for num in range(10,100,5):
#     print(num)

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for i in range(11,21,2):
    x += i
    print(i)

# for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
#     if n % 2 != 0:
#         x += n