# Challenge one: Reverse the sentence

userInput = input("Input a sentence to be reversed: ")

splitItems = userInput.split(' ')
reverseItems = []

for x in range((len(splitItems)-1), -1, -1):
	reverseItems.append(splitItems[x])

print(" ".join(reverseItems))

