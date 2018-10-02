#Counted Loop: counter to keep track
#Conditional Loop: While loop, run while statement is true

print ("***********************")
word = "";

while len(word) < 6 or word.isalpha() == False:
	word = input("Please input word longer than 5 letters: ")
	print(word.isalpha())
	if(len(word)<6):
		print("YOU IDIOT I SAID LONGER THAN 5 LETTERS")

	if (word.isalpha() == True):
		print("YOU IDIOT THATS NOT A WORD")

print(word + " is a seriously long word!")

