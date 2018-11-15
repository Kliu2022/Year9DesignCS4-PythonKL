import tkinter as tk

def create_window3():
    window3 = tk.Toplevel(root)
    window2.withdraw()
    b3 = tk.Button(window3, text="end")
    b3.pack()
    #root.deiconify()

def create_window2():
    global window2 
    window2 = tk.Toplevel(root)
    b2 = tk.Button(window2, text="Create 3", command=create_window3)
    b2.pack()
    root.withdraw()

    print("ggg")



root = tk.Tk()
b = tk.Button(root, text="Create  2  ", command=create_window2)
b.pack()

root.mainloop()