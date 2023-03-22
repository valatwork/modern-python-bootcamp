# The keyword break gives us the ability to exit out of loops whenever we want:

## example 1

while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break
    
## example 2

for x in range(1, 101):
    print(x)
    if x == 3:
        break

# adding a break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 4: 
		print("do you even listen anymore?")
		break


# exercise: generate a random number between 1 and 10, storing the result in the number variable
# every time the loop runs, increment the variable i

from random import randint  # use randint(a, b) to generate a random number between a and b
 
number = 0 #store random number in here, each time through
i = 0  # i should be incremented by one each iteration
 
while number != 5: #keep looping while number is not 5
    i += 1
    number = randint(1, 10) #update number to be a new random int from 1-10


from random import randint 
number = randint(1,10)
i = 0

while number != 5:
    i += 1
    number = randint(1, 10)