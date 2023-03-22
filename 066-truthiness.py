# In Python, all conditional checks resolve to True or False.

x = 1
x is 1  # True
x is 0  # False

# We can call values that will resolve to True "truthy", or values that will resolve to False "falsy".

# naturally false: empy objects, empty strings, None, zero

x = 1
x is 1 # True
x is 0 # False

animal = input("enter your favorite animal")

if animal:
    print(animal + " is my favorite too!")
else:
	print("YOU DIDNT SAY ANYTHING!")
