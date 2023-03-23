'''
Some APIs require a key in order for you to use them
Especially true of APIs that allow you to send data, rather than just getting data
Typically sent as part of URL
API keys allow for greater control of how users interact with the API
Instructions for obtaining a key vary by API
'''

import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored


header = figlet_format("DAD JOKE 3000!")
header = colored(header, color+"magenta")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
results= res["results"]

if num_jokes > 1:
    print(f"I found {num_jokes} about {user_input}. Here's one: ")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}")
    print(results[0]["joke"])  
else:
    print(f"Sorry, couldn't find a joke with your term: {user_input}")


# data = response.json()
# print(data["results"])
