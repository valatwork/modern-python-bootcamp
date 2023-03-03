# **kwargs
# A special operator we can pass to functions
# Gathers remaining keyword arguments as a dictionary

# example 1

def fav_colors(colt,ruby,ethel):
fav_colors(colt='purple', ruby='red', ethel='teal')

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
        
fav_colors(colt="purple", ruby="red", ethel="teal")

# example 2

def special_greeting(**kwargs):
    if "Colt" in kwargs and kwargs["Colt"] == "special":
        return "You get a special greeting Colt!"
    elif "Colt" in kwargs:
        return f"{kwargs['Colt']} Colt!"

    return "Not sure who this is..."

# special_greeting(Colt='Hello') # Hello Colt!
# special_greeting(Bob='hello') # Not sure who this is...
# special_greeting(Colt='special') # You get a special greeting Colt!
print(special_greeting(Colt='special'))