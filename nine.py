userInput = int(input("Please enter a number: "))

for x in range(1, 51):
	print("%s * %s = %s" %(userInput, x, (userInput*x)))