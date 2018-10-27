import random, string
names=[]
accounts=[]
class BankAccount:
	def __init__(self, name, deposit, PIN):
		self.name=name
		self.balance=deposit
		self.accountID=str(random.randrange(1000,9999))+(random.choice(string.ascii_uppercase))+(random.choice(string.ascii_uppercase)) # https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
		self.PIN=PIN
		self.accountStatus = "Open"
	def stats(self):
		info = "Account Holder: "+self.name
		info+= "\nAccount Balance: "+str(self.balance)
		info+= "\nAccount ID: "+self.accountID
		info+= "\nStatus: "+self.accountStatus
		return info
	def deposit(self, deposit):
		self.balance+=deposit
		status = "You successfully deposited "+str(deposit)+"."
		return status
	def withdraw(self,withdrawal):
		self.balance-=withdrawal
		status = "You successfully withdrew "+str(withdrawal)+"."
		return status
	def isClosed(self):
		self.status = "Closed"
		status = "Your account has been closed."
		return status

def start():
	global names, accounts
	name = input("\nThanks for choosing SECUREST BANK! \nPlease enter your full name. \n>>> ").title()
	if name in names:
		login(name)
	else:
		names.append(name)
		while True:
			try:
				deposit = float(input("\nLooks like you are creating a new account! \nHow much would you like to deposit? \n>>> "))
				if deposit>=0:
					if deposit>=100000:
						print("\nThatsalotta moolah! *wrings hands*")
					break
				else:
					print("\nPlease enter a positive number.")
			except ValueError:
				print("\nPlease enter a numerical value.")
		while True:
			PIN = input("\nPlease enter a five-numerical PIN of your choice \n>>> ")
			if PIN.isdigit() == True and len(PIN)==5:
					print("\nThanks! You can rest assured knowing that your PIN is encrypted with Voting-Machine-grade encryption!")
					break
			print("\nChosen PIN must only contain five digits.")
		accounts.append(BankAccount(name, deposit, PIN))
		print("\nOne moment...\n")
		print(accounts[names.index(name)].stats())
		login(name)

def login(name):
	PINA = input("\nWelcome back, "+name+"! Please login using your 5-digit PIN. \n>>> ")
	if PINA == accounts[names.index(name)].PIN:
		print("\nThanks! One moment...")
		actions(name)
	else:
		choice = input("\nWhoops! Looks like you entered your PIN incorrectly. Did you forget your PIN? (y/n) \n>>> ")
		if choice == "y":
			print("\nFine... we'll just... give it to you! Here it is: "+accounts[names.index(name)].PIN+". \nSecurest Bank: \'Love security? We do too. That's why we use Wells Fargo\'")
		elif choice == "n":
			print("\nRedirecting...")
		else:
			print("\nI don't know what that says, but for the sake of user experience, I'll just say that means no.")
		login(name)

def actions(name):
	choice =input("\nWhat would you like to do? \n(1. Deposit \n2. Withdraw \n3. Transfer \n4. Logout \nlIlI1I. Close Account) \n\n>>> ")
	if choice == "1":
		while True:
			try:
				deposit = float(input("\nWhat amount would you like to deposit? \n>>> "))
				print("\n"+accounts[names.index(name)].deposit(deposit))
				break
			except ValueError:
				print("Please enter a numerical value. We don't even care if you have the money, just don't make us confused!")
	elif choice =="2":
		while True:
			try:
				withdrawal = float(input("\nWhat amount would you like to withdraw? \n>>> "))
				if withdrawal<accounts[names.index(name)].balance:
					print("\n"+accounts[names.index(name)].withdraw(withdrawal))
					break
				else:
					print("You don't seem to have enough balance! Tough luck buddy.")
			except ValueError:
				print("Please enter a numerical value. We're giving you free money, just give us the number!")
	actions(name)
start()