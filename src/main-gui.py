import tkinter as tk
from tkinter import *
from tkinter import ttk
import hashlib
import file_handler

logged_in = False
password = ""
info = []

def login():
    user_input = userEntry.get()
    global password
    pass_input = passEntry.get()
    password = pass_input
    hashed_pass = hashlib.sha256(pass_input.encode())
    hex_pass = hashed_pass.hexdigest()
    validLogin = file_handler.verify_info(user_input, hex_pass)
    if validLogin:
        showData()
        
    else:
        incorrectLogin.pack()

def showData():
    #clear login page
    userEntry.pack_forget()
    passEntry.pack_forget()
    submitBtn.pack_forget()
    incorrectLogin.pack_forget()

    #pack container and canvas
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)


    #add login info labels    
    serviceLabel = canvas.create_text(100, 50, text="Service")
    userLabel = canvas.create_text(300, 50, text="Username")
    passLabel = canvas.create_text(500, 50, text="Password")
    canvas.create_line(0, 75, 600, 75)

    #get info as list of strings
    global info
    info = file_handler.get_info(password)
    #add login info to frame
    i = 0
    j = 0
    for line in info:
        i = 0
        j += 50
        for entry in line:
            Label(scrollable_frame, text=entry).pack(pady=5)
            #label.place(x=100+i, y=50+j)
            #scrollable_frame.create_text(100+i, 50+j, text=entry)
            i += 200
    addBtn.pack(pady=10)
    logoutBtn.pack(pady=10)

def addData():
    new_pass_window.deiconify()

def submitData():
    newService = new_serviceEntry.get()
    newUser = new_userEntry.get()
    newPass = new_passEntry.get()
    info.append([newService, newUser, newPass])
    file_handler.add_info(info, password)
    new_pass_window.withdraw()
    canvas.delete("all")
    showData()

def logout():
    #container_frame.pack_forget()
    scrollable_frame.pack_forget()
    canvas.delete("all")
    canvas.pack_forget()
    addBtn.pack_forget()
    logoutBtn.pack_forget()
    userEntry.pack(pady=10)
    passEntry.pack(pady=10)
    submitBtn.pack(pady=10)
    
#Main method -- main app execution loop
if __name__ == "__main__":
    #create root elememt
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("750x750")
    root.configure(bg='#181818')

    #add title label
    label = tk.Label(root, text="Secure Password Manager", bg='#181818')
    label.pack(pady=10)

    #Password manager login
    userEntry = tk.Entry(root, width=50)
    passEntry = tk.Entry(root, width=50, show="*")
    submitBtn = tk.Button(root, text="Submit", bg='#181818', command=login)
    incorrectLogin = tk.Label(root, text="Incorrect Password or Username", fg="red", bg='#181818')
    userEntry.pack(pady=10)
    passEntry.pack(pady=10)
    submitBtn.pack()

    #create canvas
    canvas = tk.Canvas(root, width=600, height=600, bg="#212121")

    #create inner frame and inner frame canvas for password info
    scrollable_frame = tk.Frame(canvas)
    info_canvas = tk.Canvas(scrollable_frame)
    
    #create scrollbar
    scrollbar = tk.Scrollbar(scrollable_frame, orient=VERTICAL, command=info_canvas.yview)
    info_canvas.configure(yscrollcommand=scrollbar.set)


    #create window with scrollable_frame
    canvas.create_window((0, 80), window=scrollable_frame, anchor="nw", width=600, height=520)
    scrollable_frame.bind("<Configure>", lambda e:
    canvas.configure(scrollregion=canvas.bbox("all")))


    #add-password and logout buttons
    addBtn = tk.Button(root, text="Add Password", bg='#181818', command=addData)
    logoutBtn = tk.Button(root, text="Logout", bg='#181818', command=logout)

    #add-password dialog window
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

    #run application
    root.mainloop()