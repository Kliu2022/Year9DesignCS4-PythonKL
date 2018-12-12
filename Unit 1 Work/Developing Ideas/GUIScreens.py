import tkinter as tk

def restart():
    window3.withdraw()
    root.deiconify()

def create_window3():
    global window3
    window3 = tk.Toplevel()
    #window3 = tk.Toplevel(top)
    window2.withdraw()
    b3 = tk.Button(window3, text="end", command=exit)
    b3.pack()
    b4 = tk.Button(window3, text="restart", command=restart)
    b4.pack()

def create_window2():
    global window2 
    window2 = tk.Toplevel()
    b2 = tk.Button(window2, text="Create 3", command=create_window3)
    b2.pack()
    root.withdraw()
    print("ggg")

root = tk.Tk()
b = tk.Button(root, text="Create  2  ", command=create_window2)
b.pack()

root.mainloop()