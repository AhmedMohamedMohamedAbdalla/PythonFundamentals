import os

# Created by Ahmed Mohamed Mohamed Abdalla Sleem
# 18/4/2020
# theyoungprogrammer67@gmail.com

welcomeMessage: str = "Welcome to Python Fundamentals CLI Program"
username: str = None
mainDashboard = \
	[
		'String Operations',
		'Mathematical Operations',
		'Logical Operations',
		'Type Of Your Input',
		'About Program',
		'Exit Program'
	]
stringOperationsDashboard = \
	[
		'Upper case sentence',
		'Extract SubString From String',
		'Lower Case sentence',
		'All-Caps The Whole String'
	]
mathematicalOperationsDashboard = \
	[
		'Addition',
		'Subtraction',
		'Multiplication',
		'Division',
		'Power',
		'Max',
		'Min',
		'Round',
		'Abs'
	]
logicalOperationsDashboard = \
	[
		'Is Object1 Equals Object2',
		'Is Object1 Greater/Smaller Than Object2',
		'Is Child In Parent'
	]

def printHeader(dashboard) :
	headerMsgLength: int = round(len(welcomeMessage) / 2 - len(username) / 2)
	lineLength: int = round(len('-' * len(welcomeMessage)))
	print('-' * len(welcomeMessage))
	print((' ' * headerMsgLength + username))
	if dashboard == stringOperationsDashboard :
		print(' ' * round(lineLength / 2 - len('String Operations') / 2) + 'String Operations')
		print('-' * len(welcomeMessage))
	elif dashboard == mathematicalOperationsDashboard :
		print(' ' * round(lineLength / 2 - len('Mathematical Operations') / 2) + 'Mathematical Operations')
		print('-' * len(welcomeMessage))
	elif dashboard == logicalOperationsDashboard :
		print(' ' * round(lineLength / 2 - len('Logical Operations') / 2) + 'Logical Operations')
		print('-' * len(welcomeMessage))
	else :
		print(welcomeMessage)
		print('-' * len(welcomeMessage))

def clearConsole() :
	os.system('cls' if os.name == 'nt' else 'clear')

def printDashboard(dashboard) :
	printHeader(dashboard)
	counter: int = 0
	for dashboardItem in dashboard :
		print(str(counter) + '.' + dashboardItem)
		counter += 1
	checkChoice(dashboard)

def getChoiceInput() :
	choice = input('Please Select The Number Of Your Choice With In Displayed  >> ')
	if choice.isnumeric() and not choice.isalpha() :
		choice = round(float(choice))
	else :
		choice = input('Please enter valid choice >> ')
	return choice

def checkChoice(dashboard) :
	choice: int = getChoiceInput()

	if dashboard == mainDashboard :
		if choice == 0 :
			clearConsole()
			printDashboard(stringOperationsDashboard)

		elif choice == 1 :
			clearConsole()
			printDashboard(mathematicalOperationsDashboard)

		elif choice == 2 :
			clearConsole()
			printDashboard(logicalOperationsDashboard)

		elif choice == 3 :
			clearConsole()
			resultType = input('Type what your want to get its type : ')
			if resultType.isnumeric() :
				resultType = 'Integer'
			elif resultType.isalpha() or resultType.isalnum() :
				resultType = 'String'
			else :
				resultType = 'Float'
			print('The type of your input is ' + resultType)

		elif choice == 4 :
			clearConsole()
			print('This app is coded by Ahmed Sleem @TheYoungProgrammer')

		else :
			print('Ok ' + username + '.. Thanks For Trying Python Fundamentals :)')
			exit()

	elif dashboard == stringOperationsDashboard :
		if choice == 0 :
			clearConsole()
			print(str(input('Enter the text to capitalize it ')).capitalize())

		elif choice == 1 :
			clearConsole()
			strBase1: str = input('Enter the base text to search in : ')
			searchWord: str = input('Enter the word to search : ')
			print('Text is \'' + strBase1[strBase1.find(searchWord) :len(strBase1)] + '\'')

		elif choice == 2 :
			clearConsole()
			print(str(input('Enter the text to capitalize it ')).lower())

		elif choice == 3 :
			clearConsole()
			print(str(input('Enter the text to Upper it ')).upper())

		else :
			clearConsole()
			printDashboard(mainDashboard)

	elif dashboard == mathematicalOperationsDashboard :  # afasfasfasf
		if choice == 0 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(num1 + num2))

		elif choice == 1 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(num1 - num2))

		elif choice == 2 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(num1 * num2))

		elif choice == 3 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(num1 / num2))

		elif choice == 4 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(num1 ** num2))

		elif choice == 5 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(max(num1, num2)))

		elif choice == 6 :
			clearConsole()
			num1 = int(input('Enter the first number : '))
			num2 = int(input('Enter the second number : '))
			print('Result is ' + str(min(num1, num2)))

		elif choice == 7 :
			clearConsole()
			num1 = float(input('Enter the number : '))
			print('Result is ' + str(round(num1)))

		elif choice == 8 :
			clearConsole()
			num1 = int(input('Enter the negative number : '))
			print('Result is ' + str(abs(num1)))

		else :
			clearConsole()
			printDashboard(mainDashboard)

	elif dashboard == logicalOperationsDashboard :
		if choice == 0 :
			clearConsole()
			obj1 = input('Enter first object : ')
			obj2 = input('Enter second object : ')
			if obj1 == obj2 :
				print('Both Objects are the same')
			else :
				print('Both Objects are different')
		elif choice == 1 :
			clearConsole()
			obj3 = input('Enter first object : ')
			obj4 = input('Enter second object : ')
			if obj3 > obj4 :
				print(str(obj3) + ' is greater than ' + str(obj4))
			else :
				print(str(obj3) + ' is less than ' + str(obj4))

		elif choice == 2 :
			clearConsole()
			parent = input('Enter Parent Object : ')
			child = input('Enter Child Object : ')
			if child in parent :
				print('\'' + str(child) + '\' is in \'' + parent + '\'')
			else :
				print('\'' + str(child) + '\' isn\'t in \'' + parent + '\'')
			printDashboard(mainDashboard)

		else :
			clearConsole()
			printDashboard(mainDashboard)

if __name__ == '__main__' :
	banner: str = '- ' + welcomeMessage + '.. Created By : Ahmed Sleem @TYP -'
	print('-' * len(banner))
	print(banner)
	print('-' * len(banner))
	username = str(input('Please tell me your name : '))
	printDashboard(mainDashboard)
