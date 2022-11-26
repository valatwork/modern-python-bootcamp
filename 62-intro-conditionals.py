print("What is your name?")
name = input()
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on")

# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------
 
# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
else:
    print("unlucky")

# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000)
# NO TOUCHING ======================================
 
 
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if num % 2 != 0:
    print("odd")
else:
    print("even")
