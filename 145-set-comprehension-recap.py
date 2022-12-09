# example 1
{x**2 for x in range(10)}

# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25} 
# there is no order, as this is a set

{x:x**2 for x in range(10)} # this is a dict and not a set!

# example 2

{char.upper() for char in 'hello'}
# {'E', 'H', 'L', 'O'}

# example 3

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

# breakdown

string = 'hello'

{char for char in string if char in 'aeiou'}
# {'e', 'o'}

string = 'hello hahaha'
len({char for char in string if char in 'aeiou'})
#3

len({char for char in string if char in 'aeiou'}) == 5
# False

string = 'sequoia'
len({char for char in string if char in 'aeiou'}) == 5
# True