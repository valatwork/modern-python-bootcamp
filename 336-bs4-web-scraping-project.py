'''
Introduction
In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes. 
Pick one at random and display it. The player will have four chances to guess who said the quote. 
After every wrong guess they'll get a hint about the author's identity.

Requirements
Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
You can use `bs4` and `requests` to get the data. 
For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. 
Store all of this information in a list.
Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
After each incorrect guess, the number of guesses remaining will decrement. 
If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
After every incorrect guess, the player receives a hint about the author. 
For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
The next two hints are up to you! 
Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
When the game is over, ask the player if they want to play again. 
If yes, restart the game with a new quote. If no, the program is complete.
'''

import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep

BASE_URL = "http://quotes.toscrape.com" 

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        # print(f"Now Scraping {base_url}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
    return all_quotes

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    # print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}")
        if guess == quote["author"].lower():
            print("YOU GOT IT RIGHT!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio_link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} in {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with: {['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][1]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again(y/n)?")
    if again.lower() in ('yes', 'y'):
        print("OK YOU PLAY")
        return start_game(quotes)
    else:
        print("OK, GOODBYE!")        

quotes = scrape_quotes()
start_game(quotes)