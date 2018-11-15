import tkinter as tk
import math

#You are creating a blue print to create lots of Cylinder Calculators

class CylinderCalc:




	def __init__(self):

		self.root = tk.Tk();
		self.root.title("Cylinder Calculator")

		self.labr = tk.Label(self.root, text="radius")
		self.labr.pack()

		self.entr = tk.Entry(self.root)
		self.entr.pack() 

		self.labh = tk.Label(self.root, text = "height")
		self.labh.pack()

		self.enth = tk.Entry(self.root)
		self.enth.pack()

		self.btn = tk.Button(self.root, text="Calculate", command = self.calculateVol) 
		self.btn.pack()


		self.output = tk.Text(self.root, height = 10, width = 50, borderwidth=3, relief=tk.GROOVE )
		self.output.config(state="disabled")
		self.output.pack()


		self.root.mainloop();

	def calculateVol(self):
		print("Calculating Volume")
		r = float(self.entr.get())
		h = float(self.enth.get())

		v = math.pi*r*r*h
 		outputValue = "The volume is: " + str(r)
		self.output.config(state="normal")
		self.output.insert(tk.INSERT, "TEST")
		self.output.config(state="disabled")

cylinderCalc = CylinderCalc()