import random

tries = 3

class BankAccount:

	# properties
	def __init__(self, holder_name, pin, number):
		self.number = number
		self.holder_name = holder_name
		self.pin = pin
		self.balance = 0

	#methods

	def Check_Balance (self):

		Is_Pin_Correct(pin, tries)

		print('Your balance is: ', self.balance)

	def Deposit (self, deposit_amount):

		self.balance += deposit_amount

	def Withdraw (self, withdraw_amount):

		if withdraw_amount <= self.balance:

			self.balance -= withdraw_amount

		else: 
			print('You dont have enough money.')

	def Transfer (self, transfer_to_account, transfer_amount):

		if transfer_amount <= self.balance:

			self.balance -= transfer_amount

			transfer_to_account.balance += transfer_amount

		else:

			print('You dont have enough money.')

def Is_Pin_Correct (pin, tries):
	if tries > 0:
		if pin == account_1.pin:
			pass
		
		else: 
			tries -=1
			Is_Pin_Correct(int(input('Enter PIN again: ')), tries)
	else:
		print('Your account is blocked.')
		exit()

def User_Select():

	user_choice = int(input("Choose an option: \n 1. Check balance \n 2. Deposit \n 3. Withdraw \n 4. Transfer\n"))

	if user_choice == 1:
		account_1.Check_Balance()
	elif user_choice == 2:
		account_1.Deposit(int(input('Deposit amount: ')))
	elif user_choice == 3:
		account_1.Withdraw(int(input('Withdraw amount: ')))
	elif user_choice == 4:
		account_1.Transfer(int(input('Transfer amount: ')))
	else: 
		print('Please enter acceptable values.')

	if int(input('Do you want to continue(1) or exit(2)? \n')) == 1:

		User_Select()

	else: 
		exit()	


account_1 = BankAccount("Jackson", 1234, 88888)

account_2 = BankAccount("Shostak", 3105, 77777)


print('Hello!')

pin = int(input('Please enter your PIN: '))

Is_Pin_Correct(pin, tries)

User_Select()

