age = input("How old are you: ")
# if age != ""
# if age:
#     if int(age) >= 18 and int(age) < 21:
#         print("You can enter, but need to wear a wristband!")
#     elif int(age) >= 21:
#         print("You can anter and can drink!")
#     else:
#         print("You can't come in, little one! :(")
# else:
#     print("Please enter an age!")

# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter, but need to wear a wristband!")
#     elif age >= 21:
#         print("You can anter and can drink!")
#     else:
#         print("You can't come in, little one! :(")
# else:
#     print("Please enter an age!")

# if age and (age >= 18 and age < 21):
#     print("You can enter, but need to wear a wristband!")
# elif age and age >= 21:
#     print("You can anter and can drink!")
# else:
#     print("You can't come in, little one! :(")

age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You can anter and can drink!")
    elif age >= 18:
        print("You can enter, but need to wear a wristband!")
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")

## example 1 alternate

age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 18 and age < 21: 
		print("You can enter, but need a wristband!")
	elif age >= 21:
	    print("You are good to enter and can drink!")
	else: 
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")