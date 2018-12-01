import tkinter as tk



# declaring blank variables
questionNumber = 0
attempts = 0
scoreTotal = 0
began = 0
themeNumber = 0

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

		}
		if q == 7 and a == answerKeySwitcher.get(q):
			endScreen()
			return()
		elif a == (answerKeySwitcher.get(q)):

			#Upon checking correct answer: display next question
			questionNumber += 1
			if questionNumber >= 5:
				themeNumber = 1
				question.config(background = colourBackground(themeNumber,0))
				result.config(background=colourBackground(themeNumber,0))
				mainScr.config(background = colourBackground(themeNumber, 1))
				title.config(background = colourBackground(themeNumber, 1))
				score.config(background = colourBackground(themeNumber, 1))
				scoreText.config(background = colourBackground(themeNumber, 1))
				photo2 = tk.PhotoImage(file = "The-Odyssey.ppm")
				
				imageLabel.image = photo2

				


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
	
		0: "Question 1",
		1: "Question 2",
		2: "Question 3",
		3: "Question 4",
		4: "Question 5",
		5: "Question 6",
		6: "Question 7",
		7: "Question 8",

	}	

	return questionSwitcher.get(i)

# Lookup for answer button text  
def answers(c,n):
		
	switcherA = {

		0: "Answer Choice A0",
		1: "Answer Choice A1",
		2: "Answer Choice A2",
		3: "Answer Choice A3",
		4: "Answer Choice A4",
		5: "Answer Choice A5",
		6: "Answer Choice A6",
		7: "Answer Choice A7",

	}
	switcherB = {

		0: "Answer Choice B0",
		1: "Answer Choice B1",
		2: "Answer Choice B2",
		3: "Answer Choice B3",
		4: "Answer Choice B4",
		5: "Answer Choice B5",
		6: "Answer Choice B6",
		7: "Answer Choice B7",


	}
	switcherC = {

		0: "Answer Choice C0",
		1: "Answer Choice C1",
		2: "Answer Choice C2",
		3: "Answer Choice C3",
		4: "Answer Choice C4",
		5: "Answer Choice C5",
		6: "Answer Choice C6",
		7: "Answer Choice C7",

	}


		
	switcherD = {

		0: "Answer Choice D0",
		1: "Answer Choice D1",
		2: "Answer Choice D2",
		3: "Answer Choice D3",
		4: "Answer Choice D4",
		5: "Answer Choice D5",
		6: "Answer Choice D6",
		7: "Answer Choice D7",

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

	endScr = tk.Toplevel(root)
	mainScr.withdraw()

	congrat = tk.Text(endScr)
	congrat.config(height=35, width = 104, borderwidth=3, relief=tk.GROOVE)
	congrat.config(state="normal")
	congrat.delete(1.0,tk.END)
	congrat.insert(tk.INSERT, "CONGRATULATIONS omegalul yay you sovled it ")
	congrat.config(state="disabled")

	congrat.grid(row = 0, column = 0, columnspan = 4, rowspan = 4)
	return()

# Colour Background Displayer
def colourBackground(theme, option):

	Theme0Colours = {
		0: "#FFF6CC",
		1: "#FFF4BF",
		2: "#D6C883",
	}

	Theme1Colours = {
		0: "#BED1D6",
		1: "#E3F0F3",
		2: "#9EAFBF",

	}

	if theme == 0:
		return Theme0Colours.get(option)
	if theme == 1:
		return Theme1Colours.get(option)

# main GUI
def mainScreen():

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
	global themeNumber
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

		photo1 = tk.PhotoImage(file = "The-Odyssey.ppm")
		imageLabel = tk.Label(mainScr, image = photo1)
		imageLabel.image = photo1
		imageLabel.grid(row = 1, column = 0, columnspan = 4)

		question = tk.Text(mainScr, height = 15, width = 66, borderwidth=3, relief=tk.GROOVE, background=colourBackground(themeNumber,1), font ='mincho 14')
		question.insert(tk.INSERT, questions(questionNumber))
		question.config(state="disabled")
		question.grid(row = 2, column = 0, columnspan = 4, padx=(30))

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

	beganText = tk.Text(root, height = 30, width = 80, borderwidth = 3, relief = tk.GROOVE)
	beganText.grid()

	beganButton = tk.Button(root, text="Begin!", command = mainScreen)
	beganButton.grid()


#TK MAINLOOP :)

root = tk.Tk()  

beginScreen()

root.mainloop()