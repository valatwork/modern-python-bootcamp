# We can also iterate using a while loop, which has a different format:
while im_tired
    # seek caffeine

# while loops continue to execute while a certain condition is truthy and will end when becomes falsy

user_response = None
while user_response != "please":
    user_response = input("Ah ah ah, you didn't use the magic word: ")

# the termination condition has to be speficied, and if it never becomes falsy the loop will continue forever

# msg = input("what's the secret password?")
# while msg != "bananas":
#     print("WRONG!")
#     msg = input("what's the secret password?")
# print("CORRECT!")

# for num in range(1,11):
#     print(num)

num = 1
while num < 11:
    print(num)
    num += 2