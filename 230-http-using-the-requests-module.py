'''
Lets us make HTTP requests from our Python code!
Installed using pip
Useful for web scraping/crawling, grabbing data from other APIs, etc
'''
# example 1

import requests
response = requests.get("https://news.ycombinator.com")
response # <Response [200]>
response.ok # boolean
response.headers # will retrieve the headers
response.text # will retrieve the html code

# example 2

import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"your request to {url} came back w/ status code {response.status_code}")
# your request to http://www.google.com came back w/ status code 200
print(response.text) 