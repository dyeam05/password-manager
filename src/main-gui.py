import tkinter as tk
from tkinter import *
from tkinter import ttk
import hashlib
import file_handler

logged_in = False
password = ""

def login():
    user_input = userEntry.get()
    global password
    pass_input = passEntry.get()
    password = pass_input
    hashed_pass = hashlib.sha256(pass_input.encode())
    hex_pass = hashed_pass.hexdigest()
    #print(f"user name: {user_input}")
    #print(f"pass input: {pass_input}")
    #print(f"hashed pass: {hex_pass}")
    validLogin = file_handler.verify_info(user_input, hex_pass)
    if validLogin:
        #print("successful login")
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
    serviceLabel = canvas.create_text(100, 50, text="Service")
    userLabel = canvas.create_text(300, 50, text="Username")
    passLabel = canvas.create_text(500, 50, text="Password")
    canvas.create_line(0, 75, 600, 75)
    info = file_handler.get_info(password)
    i = 0
    j = 0
    for line in info:
        i = 0
        j += 50
        for entry in line:
            canvas.create_text(100+i, 50+j, text=entry)
            i += 200
    addBtn.pack(pady=10)
    logoutBtn.pack(pady=10)        

def addData():
    new_pass_window.deiconify()

def submitData():
    newService = new_serviceEntry.get()
    newUser = new_userEntry.get()
    newPass = new_passEntry.get()
    file_handler.add_info(newService, newUser, newPass)
    new_pass_window.withdraw()
    canvas.delete("all")
    showData()

def logout():
    canvas.delete("all")
    canvas.pack_forget()
    addBtn.pack_forget()
    logoutBtn.pack_forget()
    userEntry.pack(pady=10)
    passEntry.pack(pady=10)
    submitBtn.pack(pady=10)


    
    

root = tk.Tk()
root.title("Password Manager")
root.geometry("750x750")
root.configure(bg='#181818')

label = tk.Label(root, text="Secure Password Manager", bg='#181818')
label.pack(pady=10)

userEntry = tk.Entry(root, width=50)
passEntry = tk.Entry(root, width=50, show="*")
submitBtn = tk.Button(root, text="Submit", bg='#181818', command=login)
incorrectLogin = tk.Label(root, text="Incorrect Password or Username", fg="red", bg='#181818')
userEntry.pack(pady=10)
passEntry.pack(pady=10)
submitBtn.pack()

canvas = Canvas(root, width=600, height=600, bg="#212121")
addBtn = tk.Button(root, text="Add Password", bg='#181818', command=addData)
logoutBtn = tk.Button(root, text="Logout", bg='#181818', command=logout)

new_pass_window = tk.Toplevel(root)
new_pass_window.title = ("Enter New Password")
new_pass_window.geometry("500x400")
tk.Label(new_pass_window, text="Enter Login Info").pack(pady=20)
tk.Label(new_pass_window, text="Service:").pack()
new_serviceEntry = tk.Entry(new_pass_window, width=50)
new_serviceEntry.pack(pady=10)
tk.Label(new_pass_window, text="Username:").pack()
new_userEntry = tk.Entry(new_pass_window, width=50)
new_userEntry.pack(pady=10)
tk.Label(new_pass_window, text="Password:").pack()
new_passEntry = tk.Entry(new_pass_window, width=50)
new_passEntry.pack(pady=10)
submitInfoBtn = tk.Button(new_pass_window, text="Submit", bg='#181818', command=submitData).pack(pady=10)
new_pass_window.withdraw()


"""
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame = Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
"""




root.mainloop()