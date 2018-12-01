import tkinter as tk


root = tk.Tk()


labUN = tk.Label(root, text = "User Name: ")
labUN.pack(padx = 10)

entUN = tk.Entry(root)
entUN.pack(padx = 10)

labPassword = tk.Label(root, text = "Password: ")
labPassword.pack(padx = 10)

endPassword = tk.Entry(root)
endPassword.pack(padx = 10)

btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()

#Event driven program
root.mainloop()