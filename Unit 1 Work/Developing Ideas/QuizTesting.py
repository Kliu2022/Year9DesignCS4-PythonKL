import tkinter as tk
import math

questionNumber = 0


def questions(q, a):

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
			print("CORRECT")
		else:
			#return False
			questionNumber = -1
			print("INCORRECT")
	else:

		print("Get Lost!!!")
	print(q)
	print(a)


print(questions(4,"c"))