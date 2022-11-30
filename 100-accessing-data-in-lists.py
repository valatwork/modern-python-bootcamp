friends = ["Ashley", "Matt", "Michael"]

print(friends[0]) # 'Ashley'
print(friends[2]) # 'Michael'
print(friends[3]) # IndexError

print(friends[-1]) # 'Michael'
print(friends[-3]) # 'Ashley'
print(friends[-4]) # IndexError

# check if a value is in the list, case sensitive

friends = ["Ashley", "Matt", "Michael"]

"Ashley" in friends # True

"Colt" in friends # False