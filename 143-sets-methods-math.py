# add

s = set([1, 2, 3])

s.add(4)

s # {1, 2, 3, 4}

s.add(4)

s # {1, 2, 3, 4}

# example 1

cities = {'Boulder', 'Los Angeles', 'Oslo', 'Santiago', 'Kyoto', 'San Francisco', 'Tokyo', 'Florence', 'Shanghai'}
cities.add('Vancouver')
# {'Boulder', 'Los Angeles', 'Oslo', 'Santiago', 'Kyoto', 'San Francisco', 'Tokyo', 'Vancouver', 'Florence', 'Shanghai'}

cities.remove('Oslo')
# {'San Francisco', 'Florence', 'Shanghai', 'Boulder', 'Kyoto', 'Vancouver', 'Santiago', 'Los Angeles', 'Tokyo'}

# cities.remove('Moscow')
# KeyError: 'Moscow'


# discard

cisites.discard('Moscow') # no error but nothing will happen

# copy
# it will make a duplicate of the data

s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False

# clear
# removes the entire content of the set
s = set([1, 2, 3])

s.clear()

s # set()

# set math

#Sets have quite a few other mathematical methods
# Including:
# intersection
# symmetric_difference
# union

math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

math_students | biology_students # union, no duplicates

math_students & biology_students # intersection, values that are in both data sets

# symmetric_difference

# will retun all items from both sets, excluding the ones that are present in both sets

math = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

result = math.symmetric_difference(biology)
print(result)
# {'Prashant', 'Charlotte', 'Helen', 'Jane', 'Aparna', 'Oliver', 'Mesut'}
