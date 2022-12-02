# in string interpolation, data types are implicitly converted into string form
# data types can explicitly convert variables by using the name of the builtin type as a function

decimal = 12.56345634534
integer = int(decimal) # convert float to integer

my_list = [1, 2 ,3]
convert_string = str(my_list) # convert list to string

num = 12
type(num) # check the type of the variable
num = float(num) # convert from integer to float

int(99.9999) # convert the float to integer


