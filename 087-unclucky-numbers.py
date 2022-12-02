# for num in range(1,21):
#     if num == 4 or num == 13: 
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
        
for num in range(1,21):
    if num == 4 or num == 13: 
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")

# my code
# for x in range (1,21):
#     if x == (4 or 13):                  
#         print(f"{x} is unlucky")
#     elif (x % 2) == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")