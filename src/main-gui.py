import tkinter as tk
from tkinter import *
from tkinter import ttk
import hashlib
import file_handler

logged_in = False

def login():
    user_input = userEntry.get()
    pass_input = passEntry.get()
    hashed_pass = hashlib.sha256(pass_input.encode())
    hex_pass = hashed_pass.hexdigest()
    print(f"user name: {user_input}")
    print(f"pass input: {pass_input}")
    print(f"hashed pass: {hex_pass}")
    validLogin = file_handler.verify_info(user_input, hex_pass)
    if validLogin:
        print("successful login")
        showData()
        
    else:
        incorrectLogin.pack()

def showData():
    userEntry.pack_forget()
    passEntry.pack_forget()
    submitBtn.pack_forget()
    incorrectLogin.pack_forget()
    canvas.pack() #side=LEFT, fill=BOTH, expand=True
    #scrollbar.pack(side=RIGHT, fill=Y)
    serviceLabel = canvas.create_text(100, 100, text="Service")
    userLabel = canvas.create_text(300, 100, text="Username")
    passLabel = canvas.create_text(500, 100, text="Password")
    

root = tk.Tk()
root.title("Password Manager")
root.geometry("750x750")

label = tk.Label(root, text="Secure Password Manager")
label.pack(pady=10)

userEntry = tk.Entry(root, width=50)
passEntry = tk.Entry(root, width=50, show="*")
submitBtn = tk.Button(root, text="Submit", command=login)
incorrectLogin = tk.Label(root, text="Incorrect Password or Username", fg="red")
userEntry.pack(pady=10)
passEntry.pack(pady=10)
submitBtn.pack()


canvas = Canvas(root, width=600, height=600, bg="#c5c5c5")

"""
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame = Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
"""




root.mainloop()