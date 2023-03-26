# Writing to CSV files

# using lists
# writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV

## example 1

from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    
## example 2
    
from csv import writer
# Version using writer
with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])




## example 3

from csv import reader, writer
# using nested with statements
with open('fighters.csv') as file:
	csv_reader = reader(file) #data never converted to list
	with open('screaming_fighters.csv', "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])


# Other approach, with only 1 file open at a time
with open('fighters.csv') as file:
	csv_reader = reader(file)
	# data converted to list and saved to variable
	fighters = [[s.upper() for s in row] for row in csv_reader]

with open('screaming_fighters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)
