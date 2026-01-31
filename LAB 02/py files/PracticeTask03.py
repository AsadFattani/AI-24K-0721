
class BankAccount:
	def __init__(self, owner, initial_balance=0):
		self.owner = owner
		self.__balance = initial_balance

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print(f"{self.owner}: Deposited {amount}. New balance: {self.__balance}")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			print(f"{self.owner}: Withdrew {amount}. New balance: {self.__balance}")
		else:
			print("Insufficient funds or invalid withdrawal amount.")

	def get_balance(self):
		return self.__balance

account1 = BankAccount("Amir", 100)
account2 = BankAccount("Affan", 50)

account1.deposit(50)
account1.withdraw(30)
print(f"{account1.owner}'s balance: {account1.get_balance()}")

account2.deposit(100)
account2.withdraw(200)
print(f"{account2.owner}'s balance: {account2.get_balance()}")

