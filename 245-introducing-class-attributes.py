## example 1

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"My name is {self.first_name} {self.last_name}"

    def likes(self, thing):
        return f"{self.first_name} likes {thing}!" 

p = Person("Colt", "Steele")
p.full_name()
# Colt Steele
p.likes("Python")
# Colt likes Python!

## example 2
# A User class with both a class attribute
class User:

	active_users = 0 # it's defined once

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

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




# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()

print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)
print(user2.logout())
print(User.active_users)