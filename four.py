# Challenge four: Ask the user to input a string. Ask the user what word in the string they'd like to
# replace, and with what word they'd like to replace it with.
# Output the sentence with the replacement word.

userInput = input("Please write a sentence: ").lower()
sentenceSplit = userInput.split()

while True:
	try:
		wordToReplace = input("What word would you like to replace in your sentence? ").lower()
		if wordToReplace in sentenceSplit:
			replacementWord = input("What word would you like to replace '%s' with? " %wordToReplace).lower()
			break
	except:
		print("This word does not appear in the sentence, '%s.'" %userInput)

print(userInput.replace(wordToReplace, replacementWord).capitalize())

# # <---- Try #2 with Naeem's updates :) ----->

# sentenceSplit.insert((sentenceSplit.index(wordToReplace.lower())), replacementWord)
# sentenceSplit.pop((sentenceSplit.index(wordToReplace.lower())))

# print(" ".join(sentenceSplit))
