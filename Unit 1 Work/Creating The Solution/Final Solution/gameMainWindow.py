import tkinter as tk

questionNumber = 0

def answerKey(a,b):
	return
def questions(questionNumber):
	return ("Question goes here")
def answers(a,b):
	return ("answer choice goes here")

mainScr = tk.Tk()

mainScr.configure(background='#FFF6CC')

title = tk.Text(mainScr, height = 2, width = 57, font = 'helvetica 24')
title.grid(row = 0, column = 0, columnspan = 4)

photo1 = ImageTK.PhotoImage(Image.open("The-Odyssey.jpg"))

image = tk.Label(mainScr, image = photo1)
image.grid(row = 1, column = 0, columnspan = 4)


question = tk.Text(mainScr, height = 20, width = 88, borderwidth=3, relief=tk.GROOVE, background='#FFF4BF', font ='mincho 14')
question.insert(tk.INSERT, questions(questionNumber))
question.config(state="disabled")
question.grid(row = 1, column = 0, columnspan = 4, padx=(30))

result = tk.Text(mainScr, height = 6, width = 69, borderwidth = 3, relief= tk.GROOVE, background = '#FFF4BF', font ='mincho 14')
result.config(state="disabled")
result.grid(row=2, column = 0, columnspan = 2, rowspan = 2, padx=(30,0))

answerA = tk.Button(mainScr, text=answers(0,questionNumber), height = 3, width = 40, background='#D6C883',command = lambda: answerKey(questionNumber, "a"), font ='mincho 14')
answerA.grid(row = 4, column = 0, padx = (30,0))

answerB = tk.Button(mainScr, text=answers(1,questionNumber), height = 3, width = 40, background='#D6C883',command = lambda: answerKey(questionNumber, "b"), font ='mincho 14')
answerB.grid(row = 4, column = 1, columnspan = 3, padx = (0,30))

answerC = tk.Button(mainScr, text=answers(2,questionNumber), height = 3, width = 40, background='#D6C883',command = lambda: answerKey(questionNumber, "c"), font ='mincho 14')
answerC.grid(row = 5, column = 0, padx = (30,0))

answerD = tk.Button(mainScr, text=answers(3,questionNumber), height = 3, width = 40, background='#D6C883',command = lambda: answerKey(questionNumber, "d"), font ='mincho 14')
answerD.grid(row = 5, column = 1, columnspan = 3, padx = (0,30))

scoreText = tk.Text(mainScr, height = 1, width = 6, borderwidth = 0)
scoreText.insert(tk.INSERT, "Score: ")
scoreText.config(state="disabled", background = '#FFF6CC')
scoreText.grid(row = 2, column = 2, padx = (20,0))

score = tk.Text(mainScr, height = 1, width = 5, borderwidth = 0)
score.config(state="disabled", background = '#FFF6CC')
score.insert(tk.INSERT,"score") #TEMP
score.grid(row = 2, column = 3, padx = (0,50))

tk.mainloop()

