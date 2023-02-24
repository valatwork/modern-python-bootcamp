person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {x[0]:x[1] for x in person} # my solution

# unpacking

answer = {k:v for k,v in person}

# mapping

answer = dict(person)
