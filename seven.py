while True:
	try:
		userInput = input("Please enter a number: ")
		if userInput.isdigit() == True:
			break
	except:
		print("The input is not an integer.")

for x in range(1, int(userInput)+1):
	print("*" * x)