## exercise 1

'''
For this exercise, you'll be working with a file called users.csv . 
Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:
add_user : Takes in a first name and a last name and adds a new user to the users.csv file.
'''

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

import csv
 
def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])
        
## exercise 2

'''
For this exercise, you'll be working with a file called users.csv . 
Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:
print_users : prints out all of the first and last names in the users.csv file
'''

import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))
            
            
## exercise 3

'''
For this exercise, you'll be working with a file called users.csv . 
Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. 
If the user is found, find_user  returns the index where the user is found. 
Otherwise it returns a message stating that the user wasn't found.
'''
import csv
 
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)