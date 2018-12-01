import tkinter as tk

root = tk.Tk()

output = tk.Text(root, background = "blue", height = 10, width = 50)
output.config(state="disable")
output.grid(row = 0, column = 0, columnspan = 2)

btnStat1 = tk.Button(root, text = "stat 1")
btnStat1.grid(row = 1, column = 0)

btnStat2 = tk.Button(root, text = "stat 2")
btnStat2.grid(row = 2, column = 0)

btnStat3 = tk.Button(root, text = "stat 3")
btnStat3.grid(row = 3, column = 0)

root.mainloop()