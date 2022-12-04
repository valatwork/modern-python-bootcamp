# clear empties the dictionary

d = dict(a=1,b=2,c=3)
d.clear()
d # {}

# copy makes a copy of the dictionary

d = dict(a=1,b=2,c=3)
c = d.copy()
c # {'a': 1, 'b': 2, 'c': 3}
c is d # False as they are two differnt objects

# fromkey creates key-value pairs from comma separated values:

{}.fromkeys("a","b") # {'a': 'b'}
{}.fromkeys(["email"], 'unknown') # {'email': 'unknown'}
{}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}

# new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
# new_user.fromkeys(['phone'], 'unkwown')
# new_user.fromkeys(range(1,10), 'unknown')
# new_user
# {1: 'unknown',
#  2: 'unknown',
#  3: 'unknown',
#  4: 'unknown',
#  5: 'unknown',
#  6: 'unknown',
#  7: 'unknown',
#  8: 'unknown',
#  9: 'unknown'}

# get retrieves a key in an object and return None instead of a KeyError if the key does not exist

d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1
d['b'] # 2
d.get('b') # 2
d['no_key'] # KeyError
d.get('no_key') # None