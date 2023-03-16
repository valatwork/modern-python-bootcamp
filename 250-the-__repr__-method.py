
# The most common use-case for special methods is to make classes "look pretty" in strings.

## example 1

class Human:
    pass

colt = Human()
print(colt)  # <__main__.Human at 0x1062b8400>

# The __repr__ method is one of several ways to provide a nicer string representation:

## example 2

class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name
        
dude = Human()
print(dude)  # "somebody"

# There are also several other dunders to return classes in string formats (notably __str__ and __format__), and choosing one is a bit complicated!

## example 3

class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
	# NEW CODE
	def __repr__(self):
		return f"{self.first} is {self.age}"
	# NEW CODE


	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


tom = User.from_string("Tom,Jones,89")

j = User("judy", "steele", 18)
j = str(j)
print(j)