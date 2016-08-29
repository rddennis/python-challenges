# Find the lowest common multiple of two numbers
# You failed!
# But you did find the greatest common factor
# Get it, Nesh!

numberOne = int(input("Please enter a number: "))
numberTwo = int(input("Please enter a second number: "))

numberOnePrime = []
numberTwoPrime = []
possibleGreatestCommon = []
greatestCommon = 0

for x in range(1, numberOne+1):
	if numberOne % x == 0:
		numberOnePrime.append(x)

for x in range(1, numberTwo+1):
	if numberTwo % x == 0:
		numberTwoPrime.append(x)

for x in numberOnePrime:
	if x in numberTwoPrime:
		possibleGreatestCommon.append(x)

for x in possibleGreatestCommon:
	if x > greatestCommon and x != 1:
		greatestCommon = x

print("The greatest common factor is %s." %greatestCommon)	


