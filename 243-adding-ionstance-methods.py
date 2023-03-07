# convention: write instance methods after __init__

class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        
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
		return f"Happy {self.age}th birthday, {self.first}"

    # def say_hi():
    #     print("HELLO!")


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user2.initials())
print(user1.initials())

print(user2.is_senior())
print(user1.age) #Print age before we update it
print(user1.birthday()) #updates age
print(user1.age) #Print new value of age
# user1.say_hi # TypeError: say_hi() takes 0 positional arguments but 1 was given