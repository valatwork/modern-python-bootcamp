# with blocks

## example 1

file = open("story.txt")
file.read()
file.close()

file.closed # True

## example 2

with open("story.txt") as file:
    file.read()

file.closed # True