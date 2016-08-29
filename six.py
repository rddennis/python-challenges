# Write a program that gets an integer from the user. Count from 0 to that number. Use a for loop to do it.


while True:
	try:
		userInput = input("Please enter a number: ")
		if userInput.isdigit() == True:
			break
	except:
		print("The number entered was not an integer.")

for x in range(int(userInput)+1):
	print(x)
