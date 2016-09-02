# Write a program that gets an integer from the user. Print from one to that number in astericks (*). 
# Use a for loop to do it.

while True:
	try:
		userInput = input("Please enter a number: ")
		if userInput.isdigit() == True:
			break
	except:
		print("The input is not an integer.")

for x in range(1, int(userInput)+1):
	print("*" * x)