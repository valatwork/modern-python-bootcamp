# example with fighters.csv

with open("fighters.csv") as file:
    file.read()

# this will read the module but won't parse it

'''
CSV module

reader - lets you iterate over rows of the CSV as lists
DictReader - lets you iterate over rows of the CSV as OrderedDicts
'''

# Using reader
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #To skip the headers
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}") 
     
# Example where data is cast into a list you can work with

from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

     
# Reading/Parsing CSV Using a DictReader:

from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data

# readers accept a delimiter kwargs in case the data isn't separated by commas

from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = reader(file, delimiter="|") # the pipe is just an example
    for row in csv_reader:
        print(row)