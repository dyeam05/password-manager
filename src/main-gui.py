import tkinter as tk

root = tk.Tk()
root.title("Password Manager")
root.geometry("750x750")

label = tk.Label(root, text="Secure Password Manager")
label.pack(pady=10)

root.mainloop()