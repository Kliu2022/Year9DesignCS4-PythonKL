#
import tkinter as tk

root = tk.Tk()

lab = tk.Label(root, text = "Enter a number: ")

lab.grid(row = 0, column = 0)

ent = tk.Entry(root)
ent.grid(row = 1, column = 0)

btn = tk.Button(root)
ent.grid(row = 2, column = 0)

output = tk.Text(root)
output.configure(state = "disable")
output.grid(row = 0,column = 1, rowspan = 3)



root.mainloop()
