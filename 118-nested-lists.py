nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Why?
# Complex data structures - matrices
# Game Boards / Mazes
# Rows and Columns for visualizations, tabulation and grouping data

# accessing nested list

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nested_list[0][1] # 2

nested_list[1][-1] # 6

nested_list[2][1] # 8

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# accessing values in a nested list

for l in nested_list:
    for val in l:
        print(val)


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# nested list comprehension

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(val) for val in l] for l in nested_list]

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

board = [[num for num in range(1,4)] for val in range(1,4)]

print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]

# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]


## exercise 1

'''
Using a nested list comprehension and range(), create a variable called answer  with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] .  
To break it down...start by using range and a list comp to generate the list [0,1,2].  And then repeat that whole thing 3 times in a nested list comp.  
It's all a bit tricky to discuss, so maybe it's just best to look at the solution if you get stuck.  
'''

answer = [[val for val in range(3)] for num in range(3)]

## exercise 2

'''
Using list comprehension, create a variable called answer with the following value :

[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 ]
it's a 10x10 nested list.  10 rows, each row contains the numbers 0-9.   Don't worry about the formatting/spacing, I just added a bunch of returns to make things clearer. 
Your answer will be all on one giant line. 
Use nested list comprehension and range() to accomplish this.
'''
answer = [[i for i in range(0,10)] for num in range(0,10)] 