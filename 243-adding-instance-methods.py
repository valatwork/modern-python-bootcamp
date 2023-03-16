# convention: write instance methods after __init__

class User:
	def __init__(self, first, last, age):
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
		return f"Happy {self.age}th, {self.first}"
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

## exercise

'''
Define a new class called BankAccount.  

Each BankAccount should have an owner , specified when a new BankAccount is created like BankAccount("Charlie") 
Each BankAccount should have a balance attribute  that always starts out as 0.0 
Each instance should have a deposit method that accepts a number and adds it to the balance. It should return the new balance.
Each instance should have a withdraw method that accepts a number and subtracts it from the balance. It should return the new balance.
acct = BankAccount("Darcy")
acct.owner #Darcy
acct.balance #0.0
acct.deposit(10)  #10.0
acct.withdraw(3)  #7.0
acct.balance .  #7.0

'''

# Define Bank Account Below:
class BankAccount:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance
