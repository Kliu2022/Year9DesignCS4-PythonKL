#The Odyssey Game by Kevin Liu
#Version 1.0 

#Image Credits:
#Img for welcome screen: Mosaic - Dated 2nd Century AD
#Image for questions 1-2: painting by Giovanni Domenico Tiepolo
#Image for questions 3-4: painting by Arnold Böcklin
#Image for questions 5-8: painting by Rachel McCampbell
#Image for questions 9-11: painting by Arnold Böcklin
#Image for questions 12-14: painting by Bela Čikoš Sesija

import tkinter as tk

# declaring blank variables

questionNumber = 0
attempts = 0
scoreTotal = 0
themeNumber = 0
photoNumber = 0

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

# Answer checking command, displays next question, changes themes and images  
def answerKey(q, a):

	global questionNumber
	global scoreTotal
	global attempts
	global themeNumber
	global result
	global checkStatus
	global title
	global mainScr
	global photo1
	global photo2
	global photo3
	global photo4
	global photo5

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
			if questionNumber == 8 and checkStatus.get() == 0:
				themeNumber = 1
				question.config(background = colourBackground(themeNumber,0), highlightbackground = colourBackground(themeNumber, 1))
				result.config(background=colourBackground(themeNumber,0), highlightbackground = colourBackground(themeNumber, 1))
				result.config(state="normal")
				result.delete(1.0,tk.END)
				result.insert(tk.INSERT, "You have now entered Stage 2 of the game.\n")
				result.config(state="disabled")

				mainScr.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				title.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				score.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				scoreText.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				answerA.config(highlightbackground = colourBackground(themeNumber, 1))
				answerB.config(highlightbackground = colourBackground(themeNumber, 1))
				answerC.config(highlightbackground = colourBackground(themeNumber, 1))
				answerD.config(highlightbackground = colourBackground(themeNumber, 1))


				
			if questionNumber == 12 and checkStatus.get() == 0:
				themeNumber = 2
				question.config(background = colourBackground(themeNumber,0), highlightbackground = colourBackground(themeNumber, 1))
				result.config(background=colourBackground(themeNumber,0), highlightbackground = colourBackground(themeNumber, 1))
				mainScr.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				title.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				score.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				scoreText.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
				answerA.config(highlightbackground = colourBackground(themeNumber, 1))
				result.config(state="normal")
				result.delete(1.0,tk.END)
				result.insert(tk.INSERT, "You have now entered Stage 3 of the game.\n")
				result.config(state="disabled")
				answerB.config(highlightbackground = colourBackground(themeNumber, 1))
				answerC.config(highlightbackground = colourBackground(themeNumber, 1))
				answerD.config(highlightbackground = colourBackground(themeNumber, 1))
			if questionNumber == 2:
				photoNumber == 2
				photo2 = tk.PhotoImage(file = "The-Odyssey2.ppm")
				imageLabel.config(image = photo2) 
			if questionNumber == 4:
				photoNumber == 3
				photo2 = tk.PhotoImage(file = "The-Odyssey3.ppm")
				imageLabel.config(image = photo3) 
			if questionNumber == 8:
				photoNumber == 4
				photo2 = tk.PhotoImage(file = "The-Odyssey4.ppm")
				imageLabel.config(image = photo4) 
			if questionNumber == 11:
				photoNumber == 5
				photo2 = tk.PhotoImage(file = "The-Odyssey5.ppm")
				imageLabel.config(image = photo5) 


			result.config(state="normal")
			result.delete(1.0, tk.END)
			result.insert(tk.INSERT, "Congratulations! That is correct!")
			if questionNumber == 8:
				result.insert(tk.INSERT, "\nYou have now entered Stage 2 of the game.")
			if questionNumber == 12:
				result.insert(tk.INSERT, "\nYou have now entered Stage 3 of the game.")
			result.config(state="disabled")

			scoreTotal += points(attempts)

			score.config(state="normal")
			score.delete(1.0,tk.END)
			score.insert(tk.INSERT, scoreTotal)
			score.config(state="disabled")



			question.config(state="normal")
			question.delete(1.0,tk.END)
			question.insert(tk.INSERT, questions(questionNumber))
			question.config(state="disabled")
			

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
	
		0: "Following the Trojan War, Odysseus and his crew land in the city of Ismaros (island of \nCicones). What does his crew do?",
		1: "Odysseus and his men depart from Ismaros. After sailing for 10 days, Odysseus lands on \nthe island of the lotus eaters. What do the lotus flowers do when consumed? ",
		2: "Odysseus and his men arrive at the island of the Cyclopes and were taken hostage in a \ncave, with the cyclops Polyphemus. Which of the following helped Odysseus escape?",
		3: "What is Odysseus given by Aeolus to carry him to Athens?",
		4: "However, a disobedient crewmate opens the bag of winds out of curiosity, just as Athens \ncame in sight. The winds blow Odysseus to Circe. What does Circe turn Odysseus’ men \ninto?",
		5: "Odysseus and Circe fall into a romantic trance for a year, until Odysseus’ men finally \npersuade Odysseus to leave. Where does Circe instruct Odysseus to go?",
		6: "Frightened by the spirits of the underworld, Odysseus sails back to Circe’s island, \nwhere he is directed to sail through a strait blocked by sea monsters Scylla and Charybdis. \nHe sticks to Scylla to lose only a few men rather than all of his men. How many men did he \nlose to the six-headed monster? ",
		7: "Sailing on, Odysseus stops at Thrinacia, where his men commit a fatal mistake. What is \nthis mistake?",
		8: "Odysseus, after being struck by Zeus as punishment for killing the cattle of Helios, \nfinally washes up on Calypso’s island. For how long is he stuck here for?",
		9: "Who is responsible for Calypso’s release of Odysseus?",
		10: "Odysseus finally leaves Calypso’s island, but his raft is soon destroyed by whom?",
		11: "Odysseus is washed up on the island of the Phaeacians, who hear Odysseus recount his \ntales. Through pity and admiration, what do the Phaeacians do? ",
		12: "Returning to his palace, Odysseus finds his faithful wife Penelope holding off a swarm \nof suitors looking to marry Penelope. How does Odysseus eventually prove his identity \nto Penelope? ",
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
		5: "Tiresias, the blind prophet \nof the underworld",
		6: "12 men",
		7: "Insulting the sun god Helios",
		8: "2 Years",
		9: "Athena",
		10: "Charybdis",
		11: "Bring Odysseus to Ithaca safely",
		12: "Odysseus kisses Penelope \nin a special manner",
		13: "Zeus",



	}
	switcherC = {

		0: "Stay at Ismaros to rest",
		1: "Cause memory loss and cause the \nperson to stay on the island",
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
		12: "Odysseus reveals the wedding gown \nPenelope spent years sewing",
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
		12: "Odysseus reveals that the bed in the \npalace is immobile as it is \nbuilt upon olive trees. ",
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

# For The Restart Button
def restart():
	global endScr
	global score
	global attempts
	global themeNumber
	global photoNumber
	global scoreTotal
	global questionNumber
	endScr.withdraw()
	root.deiconify()
	questionNumber = 0
	attempts = 0
	themeNumber = 0
	photoNumber = 0
	scoreTotal = 0
	score = 0

# Background Colours Lookup Displayer
def colourBackground(theme, option):

	global themeNumber
	
	ThemeAColours = {
		0: "#000000",
		1: "#000000",
		2: "#000000",
	}
	Theme0Colours = {
		0: "#FFF6CC",
		1: "#FFF4BF",
		2: "#FFF4BF",
	}

	Theme1Colours = {
		0: "#BED1D6",
		1: "#E3F0F3",
		2: "#E3F0F3",
	}
	Theme2Colours = {
		0: "#B3CD62",
		1: "#DDF39A",
		2: "#DDF39A",
	}

	if theme == -1:
		return ThemeAColours.get(option)
	if theme == 0:
		return Theme0Colours.get(option)
	if theme == 1:
		return Theme1Colours.get(option)
	else:
		return Theme2Colours.get(option)

# When game beat (endscreen) 
def endScreen():

	global mainScr
	global score
	global endScr

	endScr = tk.Toplevel(root)
	endScr.title("The Odyssey Game 1.0") 

	endScr.config(background = colourBackground(0, 1))
	mainScr.withdraw()


	title2 = tk.Text(endScr, height = 1, width = 40, font = 'helvetica 24')
	title2.insert(tk.INSERT, "The Odyssey Game")
	title2.config(state = "disabled")
	title2.config(background = colourBackground(0, 1))
	title2.grid(pady = (8,8), row = 0, column = 0, columnspan = 2)

	msg = "Congratulations! You successfully completed the game! Your score was " + str(scoreTotal) + ", out of a \npossible 1400!\n \nHopefully you had fun exploring and following the journey of Odysseus! \n \nCredits for the images used: \n\nTitle page: Mosaic dated 2nd Century AD\nImage for questions 1-2: painting by Giovanni Domenico Tiepolo\nImage for questions 3-4: painting by Arnold Böcklin\nImage for questions 5-8: painting by Rachel McCampbell\nImage for questions 9-11: painting by Arnold Böcklin\nImage for questions 12-14: painting by Bela Čikoš Sesija "

	congrat = tk.Text(endScr)
	congrat.config(height=15, width = 69, borderwidth=3, font = 'helvetica 14', relief=tk.GROOVE, background = colourBackground(0, 1), highlightbackground = colourBackground(0, 1))
	congrat.config(state="normal")
	congrat.delete(1.0,tk.END)
	congrat.insert(tk.INSERT, msg)
	congrat.config(state="disabled")
	congrat.grid(row = 1, column = 0, columnspan = 2)

	btnRestart = tk.Button(endScr)
	btnRestart.config(text = "Restart Game", command = lambda: restart())
	btnRestart.grid(row = 2, column = 0)

	btnEnd = tk.Button(endScr)
	btnEnd.config(text = "Quit Game", command = lambda: root.quit())
	btnEnd.grid(row = 2, column = 1)

# main GUI
def mainScreen():

	global themeNumber

	global accessibility

	global checkStatus

	if checkStatus.get() == 1:
		themeNumber = -1

	global mainScr

	mainScr = tk.Toplevel(root)
	mainScr.title("The Odyssey Game 1.0") 
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
	global photo1
	global photo2
	global photo3
	global photo4
	global photo5



	photo1 = tk.PhotoImage(file = "The-Odyssey1.ppm")
	photo2 = tk.PhotoImage(file = "The-Odyssey2.ppm")
	photo3 = tk.PhotoImage(file = "The-Odyssey3.ppm")
	photo4 = tk.PhotoImage(file = "The-Odyssey4.ppm")
	photo5 = tk.PhotoImage(file = "The-Odyssey5.ppm")

	mainScr.configure(background=colourBackground(themeNumber,0))

	title = tk.Text(mainScr, height = 1, width = 43, font = 'helvetica 24', highlightbackground = colourBackground(themeNumber, 1))
	title.insert(tk.INSERT, "The Odyssey Game")
	title.config(state = "disabled")
	title.grid(row = 0, column = 0, columnspan = 4, pady = (6,6))
	title.config(background = colourBackground(themeNumber, 1))
	if checkStatus.get() == 1:
		title.config(fg = "#FFFFFF")

	photo1 = tk.PhotoImage(file = "The-Odyssey1.ppm")
	imageLabel = tk.Label(mainScr, image = photo1, highlightbackground = colourBackground(themeNumber, 1))
	if photoNumber == 1:
		imageLabel.image = photo1
	elif photoNumber == 2:
		imageLabel.image = photo2
	elif photoNumber == 3:
		imageLabel.image = photo3
	elif photoNumber == 4:
		imageLabel.image = photo4
	elif photoNumber == 5:
		imageLabel.image = photo5

	
	imageLabel.grid(row = 1, column = 0, columnspan = 4)

	question = tk.Text(mainScr, height = 15, width = 66, borderwidth=3, relief=tk.GROOVE, background=colourBackground(themeNumber,1), font ='mincho 14', highlightbackground = colourBackground(themeNumber, 1))
	question.insert(tk.INSERT, questions(questionNumber))
	question.config(state="disabled")
	question.grid(row = 3, column = 0, columnspan = 4, padx=(30))
	if checkStatus.get() == 1:
		question.config(fg = "#FFFFFF")

	result = tk.Text(mainScr, height = 3, width = 52, borderwidth = 3, relief= tk.GROOVE, background=colourBackground(themeNumber,1), font ='mincho 14', highlightbackground = colourBackground(themeNumber, 1))
	result.config(state="disabled")
	result.grid(row=2, column = 0, columnspan = 2, rowspan = 1, padx=(30,0))

	answerA = tk.Button(mainScr, text=answers(0,questionNumber), height = 3, width = 30, command = lambda: answerKey(questionNumber, "a"), font ='mincho 14', highlightbackground = colourBackground(themeNumber, 1))
	answerA.grid(row = 5, column = 0, padx = (23,0))

	answerB = tk.Button(mainScr, text=answers(1,questionNumber), height = 3, width = 30, command = lambda: answerKey(questionNumber, "b"), font ='mincho 14', highlightbackground = colourBackground(themeNumber, 1))
	answerB.grid(row = 5, column = 1, columnspan = 3, padx = (0,46))

	answerC = tk.Button(mainScr, text=answers(2,questionNumber), height = 3, width = 30, command = lambda: answerKey(questionNumber, "c"), font ='mincho 14', highlightbackground = colourBackground(themeNumber, 1))
	answerC.grid(row = 6, column = 0, padx = (23,0))

	answerD = tk.Button(mainScr, text=answers(3,questionNumber), height = 3, width = 30, command = lambda: answerKey(questionNumber, "d"), font ='mincho 14', highlightbackground = colourBackground(themeNumber, 1))
	answerD.grid(row = 6, column = 1, columnspan = 3, padx = (0,46))

	scoreText = tk.Text(mainScr, height = 1, width = 6, borderwidth = 0)
	if checkStatus.get() == 1:
		scoreText.config(fg = "#FFFFFF")

	scoreText.insert(tk.INSERT, "Score: ")
	scoreText.config(state="disabled", background=colourBackground(themeNumber,0), highlightbackground = colourBackground(themeNumber, 1))
	scoreText.grid(row = 2, column = 2, padx = (15,0))

	score = tk.Text(mainScr, height = 1, width = 5, borderwidth = 0)
	score.insert(tk.INSERT, "0")
	if checkStatus.get() == 1:
		score.config(fg = "#FFFFFF")
	score.config(state="disabled", background = colourBackground(themeNumber,0), highlightbackground = colourBackground(themeNumber, 1))
	score.grid(row = 2, column = 3, padx = (0,38))

# to begin
def beginScreen():

	global photo0

	global themeNumber
	global checkStatus

	global accessibility

	acc = 0
	checkStatus = tk.IntVar()

	root.config(background = colourBackground(themeNumber, 1))

	title1 = tk.Text(root, height = 1, width = 30, font = 'helvetica 32')
	title1.insert(tk.INSERT, "The Odyssey Game")
	title1.config(state = "disabled")
	title1.grid(pady = (6,6))
	title1.config(background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))

	photo0 = tk.PhotoImage(file = "The-Odyssey0.ppm")
	beginImage = tk.Label(root, image = photo0, highlightbackground = colourBackground(themeNumber, 1))
	beginImage.image = photo0
	beginImage.grid()

	beganText = tk.Text(root, height = 10, width = 69, borderwidth = 3, font = 'helvetica 14', background = colourBackground(themeNumber, 1), highlightbackground = colourBackground(themeNumber, 1))
	beganText.insert(tk.INSERT, "Welcome to The Odyssey Game, by Kevin Liu. In this game, you will experience the \ninvigorating, three stage journey of Odysseus as he braves the natural and \nsupernatural elements haunting the seas between him and his destination. \n \nTo play, simply select the best answer to the question displayed on the screen. A\ncorrect answer is worth 100 points if obtained on the first try, 50 points on the second \ntry, 20 points on the third try, and 10 points on the last try.\n \nVisually impaired users may wish to try using the High Contrast mode below. \n \nGood luck, and have fun!")
	beganText.config(state="disabled")
	beganText.grid()

	accessibility = tk.Checkbutton(root, text="High Contrast Mode", variable = checkStatus, font = 'helvetica 14')
	accessibility.grid(pady = 6)

	beganButton = tk.Button(root, text="Begin!", command = mainScreen, height = 2, width = 30, font = 'helvetica 16')
	beganButton.grid(pady = (0,6))

#TK MAINLOOP :)

root = tk.Tk()
root.title("The Odyssey Game 1.0")  

beginScreen()

root.mainloop()