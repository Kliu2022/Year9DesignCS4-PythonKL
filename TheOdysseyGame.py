import tkinter as tk
import math

root = tk.Tk()

question = tk.Text(root, height = 10, width = 50, borderwidth=3, relief=tk.GROOVE)
question.grid(row = 0, column = 0, columnspan = 2)

answerA = tk.Button(root, text="Answer A")
answerA.grid(row = 1, column = 0)

answerB = tk.Button(root, text="Answer B")
answerB.grid(row = 1, column = 1)


answerC = tk.Button(root, text="Answer C")
answerC.grid(row = 2, column = 0)


answerD = tk.Button(root, text="Answer D")
answerD.grid(row = 2, column = 1)

root.mainloop()