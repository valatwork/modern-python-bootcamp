''' 
Writing Files

You can also use open to write to a file
Need to specify the "w" flag as the second argument
'''

# example 1

with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")
    
# IMPORTANT: If you open the file again to write, the original contents will be deleted!

# To write to a file, first open it in "w" mode
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# You can also write to files that don't yet exist
with open("lol.txt", "w") as file:
    file.write("haha" * 10000)
