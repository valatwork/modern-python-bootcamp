'''
Raise Your Own Exception!

In python we can also throw errors using the raise keyword. This is helpful when creating your own kinds of exception and error messages

'''

raise ValueError('invalid value')

# example

def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

colorize([], 'cyan')
# colorize(34, "red")