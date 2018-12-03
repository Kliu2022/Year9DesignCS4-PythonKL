import tkinter as tk

# declaring blank variables
questionNumber = 0
attempts = 0
scoreTotal = 0
began = 0
themeNumber = 0
acc = 0


# Score Counter 
def points(k):

	global attempts
	k = attempts

	if attempts > 3: 
		return 0

	switcherScore = {
	0: "100",
	1: "50",
	2: "20",
	3: "10",
	}

	return int(switcherScore.get(k))

# Answer checking command  
def answerKey(q, a):

	global questionNumber
	global scoreTotal
	global attempts
	global themeNumber
	global title
	global mainScr
	global photo2

	if q != -1:

		answerKeySwitcher = {

			0: "a",
			1: "c",
			2: "a",
			3: "b",
			4: "a",
			5: "b",
			6: "d",
			7: "d",
			8: "a",
			9: "c",
			10: "c",
			11: "b",
			12: "d",
			13: "a",


		}
		if q == 13 and a == answerKeySwitcher.get(q):
			scoreTotal += points(attempts)
			endScreen()
			return()
		elif a == (answerKeySwitcher.get(q)):

			#Upon checking correct answer: display next question
			questionNumber += 1
			if questionNumber == 8:
				themeNumber = 1
				question.config(background = colourBackground(themeNumber,0))
				result.config(background=colourBackground(themeNumber,0))
				mainScr.config(background = colourBackground(themeNumber, 1))
				title.config(background = colourBackground(themeNumber, 1))
				score.config(background = colourBackground(themeNumber, 1))
				scoreText.config(background = colourBackground(themeNumber, 1))

				photo2 = tk.PhotoImage(file = "The-Odyssey2.ppm")
				imageLabel.config(image = photo2) 
			if questionNumber == 12:
				themeNumber = 2
				question.config(background = colourBackground(themeNumber,0))
				result.config(background=colourBackground(themeNumber,0))
				mainScr.config(background = colourBackground(themeNumber, 1))
				title.config(background = colourBackground(themeNumber, 1))
				score.config(background = colourBackground(themeNumber, 1))
				scoreText.config(background = colourBackground(themeNumber, 1))


			question.config(state="normal")
			question.delete(1.0,tk.END)
			question.insert(tk.INSERT, questions(questionNumber))
			question.config(state="disabled")
			#Display "Correct"
			result.config(state="normal")
			result.delete(1.0,tk.END)
			result.insert(tk.INSERT, "Congratulations! That is correct!")
			result.config(state="disabled")

			#for the score counter
			scoreTotal += points(attempts)

			score.config(state="normal")
			score.delete(1.0,tk.END)
			score.insert(tk.INSERT, scoreTotal)
			score.config(state="disabled")

			#updating answer choices
			answerA.config(text=answers(0,questionNumber))
			answerB.config(text=answers(1,questionNumber))
			answerC.config(text=answers(2,questionNumber))
			answerD.config(text=answers(3,questionNumber))
			answerA.config(state="normal", background="#D3D3D3")
			answerB.config(state="normal", background="#D3D3D3")
			answerC.config(state="normal", background="#D3D3D3")
			answerD.config(state="normal", background="#D3D3D3")

			#clearing attempts counter
			attempts = 0

		elif a != (answerKeySwitcher.get(q)):
			#return False

			attempts += 1

			if a == "a":
				answerA.config(state="disabled", background="#A9A9A9")
			if a == "b":
				answerB.config(state="disabled", background="#A9A9A9")
			if a == "c":
				answerC.config(state="disabled", background="#A9A9A9")
			if a == "d":
				answerD.config(state="disabled", background="#A9A9A9")

			result.config(state="normal")
			result.delete(1.0,tk.END)
			result.insert(tk.INSERT, "Uh oh. That is incorrect. Try Again...")
			
			result.config(state="disabled")

# Display question switcher  
def questions(i):
	
	questionSwitcher = {
	
		0: "Odysseus and his crew land in the city of Ismaros (island of Cicones). What does his crew do?",
		1: "After being at sea for 10 days, Odysseus lands on the island of the lotus eaters. What do the lotus flowers do when consumed? ",
		2: "Odysseus and his men arrive at the island of the Cyclopes and were taken hostage in a cave, with the cyclops Polyphemus. Which of the following helped Odysseus escape?",
		3: "What is Odysseus given by Aeolus to carry him to Athens?",
		4: "However, a disobedient crewmate opens the bag of winds out of curiosity, just as Athens came in sight. The winds blow Odysseus to Circe. What does Circe turn Odysseus’ men into?",
		5: "Odysseus and Circe fall into a romantic trance for a year, until Odysseus’ men finally persuade Odysseus to leave. Where does Circe instruct Odysseus to go?",
		6: "Frightened by the spirits of the underworld, Odysseus sails back to Circe’s island, where he is directed to sail through a strait blocked by sea monsters Scylla and Charybdis. He sticks to Scylla to lose only a few men rather than all of his men. How many men did he lose to the six-headed monster? ",
		7: "Sailing on, Odysseus stops at Thrinacia, where his men commit a fatal mistake. What is this mistake?",
		8: "Odysseus, after being struck by Zeus as punishment for killing the cattle of Helios, finally washes up on Kalypso’s island. For how long is he stuck here for?",
		9: "Who is responsible for Kalypso’s release of Odysseus?",
		10: "Odysseus finally leaves Kalypso’s island, but his raft is soon destroyed by whom?",
		11: "Odysseus is washed up on the island of the Phaeacians, who hear Odysseus recount his tales. Through pity and admiration, what do the Phaeacians do? ",
		12: "Returning to his palace, Odysseus finds his faithful wife Penelope holding off a swarm of suitors looking to marry Penelope. How does Odysseus eventually prove his identity to Penelope? ",
		13: "Who eventually restored peace in the palace?",


	}	

	return questionSwitcher.get(i)

# Lookup for answer button text  
def answers(c,n):
		
	switcherA = {

		0: "Raid the city",
		1: "Poison the person",
		2: "Some wine",
		3: "A compass",
		4: "Swine",
		5: "Poseidon, god of the sea",
		6: "All of his men",
		7: "Forgetting to make a sacrifice to Zeus",
		8: "7 Years",
		9: "Poseidon",
		10: "Scylla",
		11: "Threaten to kill Odysseus",
		12: "Odysseus tells his story to Penelope",
		13: "Athena",


	}
	switcherB = {

		0: "Sail away",
		1: "Nothing",
		2: "A sword",
		3: "A bag of winds",
		4: "Stone",
		5: "Tiresias, the blind prophet of the underworld",
		6: "12 men",
		7: "Insulting the sun god Helios",
		8: "2 Years",
		9: "Athena",
		10: "Charybdis",
		11: "Bring Odysseus to Athens safely",
		12: "Odysseus kisses Penelope in a special manner",
		13: "Zeus",



	}
	switcherC = {

		0: "Stay at Ismaros to rest",
		1: "Cause memory loss and cause the person to stay on the island",
		2: "A flock of birds",
		3: "Hermes' boots",
		4: "Dust",
		5: "Polyphemus, the valiant cyclops",
		6: "8 men",
		7: "Destroying the temple of Thrinacia",
		8: "7 Months",
		9: "Zeus",
		10: "Poseidon",
		11: "Allow Odysseus to stay with them",
		12: "Odysseus reveals the wedding gown Penelope spent years sewing",
		13: "Hermes",
	

	}


		
	switcherD = {

		0: "Wage war against the city",
		1: "Cause person to fall in a deep slumber",
		2: "A giant boulder",
		3: "A magical bow",
		4: "Sheep",
		5: "Hermes, the messenger god",
		6: "6 men",
		7: "Killing the sacred cattle of Helios",
		8: "1 Year",
		9: "Circe",
		10: "Zeus",
		11: "Report Odysseus' location to Poseidon",
		12: "Odysseus reveals that the bed in the palace is immobile as it is built upon olive trees. ",
		13: "The Sirens",


	}

	if c == 0:
		return switcherA.get(n)
	if c == 1:
		return switcherB.get(n)
	if c == 2:
		return switcherC.get(n)
	if c == 3:
		return switcherD.get(n)

# When game beat (endscreen) 
def endScreen():

	global mainScr
	global score

	endScr = tk.Toplevel(root)

	endScr.config(background = colourBackground(0, 1))
	mainScr.withdraw()


	title2 = tk.Text(endScr, height = 2, width = 40, font = 'helvetica 24')
	title2.insert(tk.INSERT, "The Odyssey Game")
	title2.config(state = "disabled")
	title2.config(background = colourBackground(0, 1))
	title2.grid()

	msg = "Congratulations! You successfully completed the game! Your score was " + str(scoreTotal) + "!"



	congrat = tk.Text(endScr)
	congrat.config(height=15, width = 69, borderwidth=3, font = 'helvetica 14', relief=tk.GROOVE)
	congrat.config(state="normal")
	congrat.delete(1.0,tk.END)
	congrat.insert(tk.INSERT, msg)
	congrat.config(state="disabled")

	congrat.grid()
	return()

# Colour Background Displayer
def colourBackground(theme, option):

	global themeNumber

	print(themeNumber)

	
	ThemeAColours = {
		0: "#FFFFFF",
		1: "#000000"
	}
	Theme0Colours = {
		0: "#FFF6CC",
		1: "#FFF4BF",
	}

	Theme1Colours = {
		0: "#BED1D6",
		1: "#E3F0F3",
	}
	Theme2Colours = {
		0: "#B3CD62",
		1: "#DDF39A"
	}

	if theme == -1:
		return ThemeAColours.get(option)
	if theme == 0:
		return Theme0Colours.get(option)
	if theme == 1:
		return Theme1Colours.get(option)
	else:
		return Theme2Colours.get(option)

# main GUI
def mainScreen():

	global themeNumber
	print(themeNumber)

	global mainScr

	mainScr = tk.Toplevel(root)
	root.withdraw()

	global questionNumber
	global question
	global result
	global answerA
	global answerB
	global answerC
	global answerD
	global scoreText
	global score
	global answerKey
	global title
	global imageLabel

	if questionNumber >= 8: 
		endScreen()
	else: 

		mainScr.configure(background=colourBackground(themeNumber,0))

		title = tk.Text(mainScr, height = 2, width = 43, font = 'helvetica 24')
		title.insert(tk.INSERT, "The Odyssey Game")
		title.config(state = "disabled")
		title.grid(row = 0, column = 0, columnspan = 4)
		title.config(background = colourBackground(themeNumber, 1))
		if acc == 1:
			title.config(fg = "#FFFFFF")

		photo1 = tk.PhotoImage(file = "The-Odyssey.ppm")
		imageLabel = tk.Label(mainScr, image = photo1)
		if themeNumber == 0:
			imageLabel.image = photo1
		elif themeNumber == 1:
			imageLabel.image = photo2
		
		imageLabel.grid(row = 1, column = 0, columnspan = 4)

		question = tk.Text(mainScr, height = 15, width = 66, borderwidth=3, relief=tk.GROOVE, background=colourBackground(themeNumber,1), font ='mincho 14')
		question.insert(tk.INSERT, questions(questionNumber))
		question.config(state="disabled")
		question.grid(row = 2, column = 0, columnspan = 4, padx=(30))
		if acc == 1:
			question.config(fg = "#FFFFFF")

		result = tk.Text(mainScr, height = 3, width = 52, borderwidth = 3, relief= tk.GROOVE, background=colourBackground(themeNumber,1), font ='mincho 14')
		result.config(state="disabled")
		result.grid(row=3, column = 0, columnspan = 2, rowspan = 2, padx=(30,0))

		answerA = tk.Button(mainScr, text=answers(0,questionNumber), height = 3, width = 30, background=colourBackground(themeNumber,1),command = lambda: answerKey(questionNumber, "a"), font ='mincho 14')
		answerA.grid(row = 5, column = 0, padx = (23,0))

		answerB = tk.Button(mainScr, text=answers(1,questionNumber), height = 3, width = 30, background=colourBackground(themeNumber,1),command = lambda: answerKey(questionNumber, "b"), font ='mincho 14')
		answerB.grid(row = 5, column = 1, columnspan = 3, padx = (0,23))

		answerC = tk.Button(mainScr, text=answers(2,questionNumber), height = 3, width = 30, background=colourBackground(themeNumber,1),command = lambda: answerKey(questionNumber, "c"), font ='mincho 14')
		answerC.grid(row = 6, column = 0, padx = (23,0))

		answerD = tk.Button(mainScr, text=answers(3,questionNumber), height = 3, width = 30, background=colourBackground(themeNumber,1),command = lambda: answerKey(questionNumber, "d"), font ='mincho 14')
		answerD.grid(row = 6, column = 1, columnspan = 3, padx = (0,23))

		scoreText = tk.Text(mainScr, height = 1, width = 6, borderwidth = 0)
		scoreText.insert(tk.INSERT, "Score: ")
		scoreText.config(state="disabled", background=colourBackground(themeNumber,0))
		scoreText.grid(row = 3, column = 2, padx = (15,0))

		score = tk.Text(mainScr, height = 1, width = 5, borderwidth = 0)
		score.config(state="disabled", background = colourBackground(themeNumber,0))
		score.grid(row = 3, column = 3, padx = (0,38))


# to begin
def beginScreen():

	global themeNumber

	acc = 0

	root.config(background = colourBackground(themeNumber, 1))

	title1 = tk.Text(root, height = 2, width = 40, font = 'helvetica 24')
	title1.insert(tk.INSERT, "The Odyssey Game")
	title1.config(state = "disabled")
	title1.grid(row = 0, column = 0, columnspan = 4)
	title1.config(background = colourBackground(themeNumber, 1))

	beganText = tk.Text(root, height = 10, width = 69, borderwidth = 3, font = 'helvetica 14', background = colourBackground(themeNumber, 1))
	beganText.insert(tk.INSERT, "Welcome to The Odyssey Game, by Kevin Liu. In this game, you will experience the \ninvigorating, three stage journey of Odysseus as he braves the natural and \nsupernatural elements haunting the seas between him and his destination. \n \n To play, simply select the best answer to the question displayed on the screen. \n \n If you are visually impaired, try using the 'High Contrast Mode' feature below. \n \n Good luck, and have fun!")
	beganText.config(state="disabled")
	beganText.grid()

	accessibility = tk.Checkbutton(root, text="High Contrast Mode", variable = acc, onvalue = -1, offvalue = 0, font = 'helvetica 14')
	accessibility.grid(pady = 6)

	if acc == -1:
		themeNumber = -1

	beganButton = tk.Button(root, text="Begin!", command = mainScreen, height = 2, width = 30, font = 'helvetica 16')
	beganButton.grid(pady = (0,6))

#TK MAINLOOP :)

root = tk.Tk()  

beginScreen()

root.mainloop()