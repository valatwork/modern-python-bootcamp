# print("How many kilometers did you cycle today?")
# kms = input() #this is a string right now
# print("Okay, you said 10" + kms)

# print("How many kilometers did you cycle today?")
# kms = float(input()) # converting kms into a float
# print("Okay, you said 10" + kms)

# print("How many kilometers did you cycle today?")
# kms = input()
# float(kms) # another way to convert kms into a float
# print("Okay, you said 10" + kms)

# print("How many kilometers did you cycle today?")
# kms = input()
# miles = float(kms)/1.60934
# print(f"That is equal to {miles} miles ")
# # this will print a lot of decimals

# print("How many kilometers did you cycle today?")
# kms = input()
# miles = float(kms)/1.60934
# print(f"That is equal to {round(miles,2)} miles ") # round to 2 decimals

# print("How many kilometers did you cycle today?")
# kms = input()
# miles = float(kms)/1.60934
# miles = round(miles, 2) # round to 2 decimals
# print(f"That is equal to {miles} miles ")

print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was {miles}mi ") # nicer output
