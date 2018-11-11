import tkinter as tk

began = 0
questionNumber = 0

def init():
	global began
	began += 1
	return()

def checkAnswer():
	global questionNumber
	questionNumber += 1


# to begin
def beginScreen():


	beganButton = tk.Button(root, text="Begin!", command = init())
	beganButton.grid()

def mainScreen():


	#beganButton.grid_forget()
	button = tk.Button(root, text = "Mainscreen!", command = checkAnswer())
	button.grid()

def endScreen():

	button.grid_forget()

	text = tk.Text(text = "end screen")

root = tk.Tk()


if questionNumber >= 1:

	endScreen()
elif 1 == 1:

	mainScreen()

#else:
#	beginScreen()

tk.mainloop()