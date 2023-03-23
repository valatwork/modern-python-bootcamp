'''
What's a Query String?

A way to pass data to the server as part of a GET request
http://www.example.com/?key1=value1&key2=value2
Browsers enforce a maximum size on length of the query string
'''

## example 1

import requests

response = requests.get(
    "http://www.example.com?key1=value1&key2=value2"
)

## example 2 - preferable!

import requests

response = requests.get(
    "http://www.example.com",
    params={
        "key1": "value1",
        "key2": "value2"
    }
)

## example 3

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
)

data = response.json()
print(data["results"])

## example 4 POST request

import requests
import json

response = requests.post(
    "http://www.example.com",
    data=json.dumps({
        "key1": "value1",
        "key2": "value2"
    })
)