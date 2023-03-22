'''
Given a person variable:

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]] 

Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value.  T
hat's a terrible explanation.  
I think it'll be easier if you just look at the end goal:

{'name': 'Jared', 'job': 'Musician', 'city': 'Bern'} 

There are many potential solutions for this.
'''

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {x[0]:x[1] for x in person} # my solution

# unpacking

answer = {k:v for k,v in person}

# mapping

answer = dict(person)
