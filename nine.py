# Ask the user to input a number, then print the multiplication table for that number from 1 to 50.

userInput = int(input("Please enter a number: "))

for x in range(1, 51):
	print("%s * %s = %s" %(userInput, x, (userInput*x)))