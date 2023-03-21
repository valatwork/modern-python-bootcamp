'''
Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses from a popular song about a the beverage. 
The number of verses in the song is determined by the count. 

Each verse of the song should involve one fewer beverage, until there are no beverages remaining. 
(Check the examples for details on the structure of the lyrics.)

The default count should be 99, and the default beverage should be soda.

'''

def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)