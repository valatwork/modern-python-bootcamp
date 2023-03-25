'''
Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file. 

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. 
This is also the text used in the tests.

copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

## exercise 1

'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)
        
        
## exercise 2

'''
Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
'''

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

## exercise 3

'''
Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
'''

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }
    
    
## exercise 4

'''
Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. 
Replaces all instances of the word in the file with the replacement word.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. 
This is also the text used in the tests.)
'''

'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()