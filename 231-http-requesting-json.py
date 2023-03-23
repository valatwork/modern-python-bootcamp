# making a request

import requests

response = requests.get("http://www.example.com")

# request headers

import requests

response = requests.get(
    "http://www.example.com",
    headers={
        "header1": "value1",
        "header2": "value2"
    }
)

## example 1

import requests
url = "http://icanhazdadjoke.com"

response = requests.get(url, headers={"Accept": "text/plain"})

print(response.text)

## example with JSON

import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

print(response.text)
# it looks like a dict but it is actually a str
# {"id":"2Luc21TSnb","joke":"Have you heard the story about the magic tractor? It drove down the road and turned into a field.","status":200}
print(response.json())
# {'id': '2Luc21TSnb', 'joke': 'Have you heard the story about the magic tractor? It drove down the road and turned into a field.', 'status': 200}
data = response.json()
print(type(data)) # <class 'dict'>
print(data["joke"])
# What do you get when you cross a chicken with a skunk? A fowl smell!

## JSON continued

import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(data["joke"])
print(f"status: {data['status']}")

# How do locomotives know where they're going? Lots of training
# status: 200


