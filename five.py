# Write a program at generates a random 7 digit number and add all of the prime digits in the number.
# Time Limit: 45 minutes + 20 minutes
# Input - None
# Process - Program must generate a random 7 digit number, then add all of the prime number together.
# Output - The original number and the sum of the prime numbers


from random import randint

randNum = str(randint(1000000,10000000))
primeNumbers = []
primeTotal = 0

for x in range(7):
	divCounter = 0
	for i in range(1,10):
		if (int(randNum[x]) % i == 0):
			divCounter += 1
	
	if divCounter == 1 or divCounter == 2:
		primeNumbers.append(int(randNum[x]))

for x in primeNumbers:
	primeTotal = primeTotal + x

print("The original number was %s.\nThe prime numbers in this number are %s. \nThe total of all prime numbers is %s." %(randNum, primeNumbers, primeTotal))