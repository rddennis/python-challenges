# Challenge two: Find the longest sentence in the word.

userInput = input("Please enter a sentence: ")
inputList = userInput.split(" ")
longestWord = " "

for x in inputList:
	if len(x) > len(longestWord):
		longestWord = x

print("The longest word in your sentence is \"%s\"." %longestWord)