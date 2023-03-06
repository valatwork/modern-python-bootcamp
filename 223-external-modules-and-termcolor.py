'''
External Modules

Built-in modules come with Python
External modules are downloaded from the internet
You can download external modules using pip

'''

# pip

'''
Package management system for Python
As of 3.4, comes with Python by default
python3 -m pip install NAME_OF_PACKAGE

'''

# examples

'''
termcolor - Adds colors to output in a Python shell
pyfiglet - Ascii art creator!

'''

'''
colors.py

from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)

'''

from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "magenta"

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)

