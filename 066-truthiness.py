# naturally false: empy objects, empty strings, None, zero

x = 1
x is 1 # True
x is 0 # False

animal = input("enter your favorite animal")

if animal:
    print(animal + " is my favorite too!")
else:
	print("YOU DIDNT SAY ANYTHING!")
