'''
When run, every Python file has a __name__ variable
If the file is the main file being run, its value is "__main__"
Otherwise, its value is the file name

'''

## file 1

say_hi.py

def say_hi():
    print(f"HI! My __name__ is {__name__}")
say_hi()

## file 2
say_sup.py

def say_sup():
    print(f"SUP! My __name__ is {__name__}")
say_sup()

# SUP! MY __name__ is __main__

## combining
say_hi.py

from say_sup import say_sup
def say_hi():
    print(f"HI! My __name__ is {__name__}")
say_hi()
say_sup()

# SUP! MY __name__ is say_sup
# HI! My __name__ is __main__
# SUP! My __name__ is say_sup

'''
When using import Python

1. Tries to find the module (if it fails, it throws an error),
2. Runs the code inside of the module being imported,
3. Creates variables in the namespace of the file with the import statement.

'''

## ignoring code on import

if __name__ == "__main__":
    # this code will only run
    # if the file is the main file!

## combining fixed

say_sup.py

def say_sup():
    print(f"SUP! My __name__ is {__name__}")
if __name__ == "__main__":
    say_sup()

# executing say_hi.py
# HI! My __name__ is __main__
# SUP! My __name__ is say_sup

# excuting say_sup.py
# SUP! My __name__ is __main__