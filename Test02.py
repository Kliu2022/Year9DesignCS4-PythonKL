import tkinter as tk

scr1 = 1


def GoToSecondScreen():
	global scr1
	scr1 = 2
	print(scr1)


def GoToThirdScreen():
	global scr1
	scr1 = 3


def screen1():
	global button1
	button1 = tk.Button(text="Begin", command = lambda: GoToSecondScreen())
	button1.grid()

def screen2():
	global button2
	button1.grid_forget()
	button2 = tk.Button(text="Screen 2", command = lambda: GoToThirdScreen())
	button2.grid()

def screen3():
	global button3
	button2.grid_forget()
	button3 = tk.Button(text="Screen 3")
	button3.grid()


root = tk.Tk()

if scr1 == 1: 
	screen1()
elif scr1 == 2:
	screen2()
elif scr1 == 3:
	screen3()

tk.mainloop() 