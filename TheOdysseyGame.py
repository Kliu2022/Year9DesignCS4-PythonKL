import tkinter as tk
import math

questionNumber = 0
attempts = 0
scoreTotal = 0


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

	print(q)
	print(a)
	if q != -1:


		switcher = {
		0: "a",
		1: "c",
		2: "a",
		3: "b",
		4: "a",
		5: "b",
		6: "d",
		7: "d",

		}

		if a == (switcher.get(q)):
		
			#checking a correct answer also displays the next question
			questionNumber += 1
			question.config(state="normal")
			question.delete(1.0,tk.END)
			question.insert(tk.INSERT, questions(questionNumber))
			question.config(state="disabled")
			#Correct Display
			result.config(state="normal")
			result.delete(1.0,tk.END)
			result.insert(tk.INSERT, "Congratulations! That is correct!")
			result.config(state="disabled")

			scoreTotal += points(attempts)

			score.config(state="normal")
			score.delete(1.0,tk.END)
			score.insert(tk.INSERT, scoreTotal)
			score.config(state="disabled")

			answerA.config(text=answers(0,questionNumber))
			answerB.config(text=answers(1,questionNumber))
			answerC.config(text=answers(2,questionNumber))
			answerD.config(text=answers(3,questionNumber))
			
			attempts = 0


		elif a != (switcher.get(q)):
			#return False
		

			attempts += 1
			result.config(state="normal")
			result.delete(1.0,tk.END)
			result.insert(tk.INSERT, "Uh oh. That is incorrect. Try Again...")
			
			result.config(state="disabled")
	else:

		return("Get Lost!!!")

#Display question switcher
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

# For text on answer buttons
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


#TK MAINLOOP 

root = tk.Tk()


question = tk.Text(root, height = 20, width = 104, borderwidth=3, relief=tk.GROOVE)
question.insert(tk.INSERT, questions(questionNumber))
question.config(state="disabled")
question.grid(row = 0, column = 0, columnspan = 4)

result = tk.Text(root, height = 6, width = 68, borderwidth = 3, relief= tk.GROOVE)
question.config(state="disabled")
result.grid(row=1, column = 0, columnspan = 2, rowspan = 2)

answerA = tk.Button(root, text=answers(0,questionNumber), height = 3, width = 40, command = lambda: answerKey(questionNumber, "a"))
answerA.grid(row = 3, column = 0)

answerB = tk.Button(root, text=answers(1,questionNumber), height = 3, width = 40, command = lambda: answerKey(questionNumber, "b"))
answerB.grid(row = 3, column = 1, columnspan = 3)

answerC = tk.Button(root, text=answers(2,questionNumber), height = 3, width = 40, command = lambda: answerKey(questionNumber, "c"))
answerC.grid(row = 4, column = 0)

answerD = tk.Button(root, text=answers(3,questionNumber), height = 3, width = 40, command = lambda: answerKey(questionNumber, "d"))
answerD.grid(row = 4, column = 1, columnspan = 3)

scoreText = tk.Text(root, height = 3, width = 13)
scoreText.insert(tk.INSERT, "Score: ")
scoreText.config(state="disabled")
scoreText.grid(row = 1, column = 2)

score = tk.Text(root, height = 3, width = 13)
score.config(state="disabled")
score.grid(row = 1, column = 3)


root.mainloop()


