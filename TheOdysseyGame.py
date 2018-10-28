import tkinter as tk
import math

questionNumber = 0

# To 
def answerKey(q, a):

	global questionNumber

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
			#return True
			questionNumber += 1
			return("CORRECT")
		elif a != (switcher.get(q)):
			#return False
			q = -1
			return("INCORRECT")
	else:

		return("Get Lost!!!")

def questions:

	
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


root = tk.Tk()



question = tk.Text(root, height = 10, width = 50, borderwidth=3, relief=tk.GROOVE)
question.grid(row = 0, column = 0, columnspan = 2)
question.insert(tk.INSERT, lambda: print(questionSwitcher.get(questionNumber)))

answerA = tk.Button(root, text="Answer A", command = lambda: print(answerKey(questionNumber,"a")))
answerA.grid(row = 1, column = 0)

answerB = tk.Button(root, text="Answer B", command = lambda: print(answerKey(questionNumber,"b")))
answerB.grid(row = 1, column = 1)


answerC = tk.Button(root, text="Answer C", command = lambda: print(answerKey(questionNumber,"c")))
answerC.grid(row = 2, column = 0)


answerD = tk.Button(root, text="Answer D", command = lambda: print(answerKey(questionNumber,"d")))
answerD.grid(row = 2, column = 1)

root.mainloop()


