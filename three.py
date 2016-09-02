# Challenge three: Write a program that finds duplicate letters in a word or sentence.

userInput = input("Please enter a word or sentence: ").lower()
repeatedLetters = []
x = 0
length = len(userInput)

while True:
	if userInput.isdigit() == True:
		userInput = input("Hmmm... That doesn't seem like it's a word. Please enter a word or sentence: ")
	else:
		break

while x < length:
	if userInput.count(userInput[x]) > 1 and userInput[x] not in repeatedLetters and (userInput[x].isalpha() == True):
		print("%s appears %s times in \"%s\"." %(userInput[x], userInput.count(userInput[x]), userInput.capitalize()))
		repeatedLetters.append(userInput[x])	
	x += 1

# for x in range(len(userInput)):
# 	if userInput.count(userInput[x]) > 1 and userInput[x] not in repeatedLetters and (userInput[x].isalpha() == True):
# 		print("%s appears %s times in \"%s\"" %(userInput[x], userInput.count(userInput[x]), userInput))
# 		repeatedLetters.append(userInput[x])	

if repeatedLetters == []:
	print("There were no repeated letters in \"%s\"." %userInput.capitalize())

	