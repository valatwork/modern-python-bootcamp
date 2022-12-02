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