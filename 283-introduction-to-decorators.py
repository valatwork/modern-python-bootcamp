'''
What's a decorator?

Decorators are functions
Decorators wrap other functions and enhance their behavior
Decorators are examples of higher order functions
Decorators have their own syntax, using "@" (syntactic sugar)

'''

# example 1

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Colt.")

def rage():
	print("I HATE YOU!")

greet = be_polite(greet)
greet()
polite_rage = be_polite(rage)
polite_rage()

# decorator syntax

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")


@be_polite
def rage():
	print("I HATE YOU!")


greet()
rage()