import tkinter as tk
from tkinter import *
from tkinter import ttk
import hashlib
import file_handler

logged_in = False
password = ""
info = []


#Checks credentials for login authentication
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

#Clears login page and shows decrypted password information
def showData():
    #clear login page
    userEntry.pack_forget()
    passEntry.pack_forget()
    submitBtn.pack_forget()
    incorrectLogin.pack_forget()

    #pack container and canvas
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    #scrollable_frame.pack()
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

#Opens dialog box to add password data
def addData():
    new_pass_window.deiconify()

#Submits password data to decrypted bytestream in memory
def submitData():
    newService = new_serviceEntry.get()
    newUser = new_userEntry.get()
    newPass = new_passEntry.get()
    info.append([newService, newUser, newPass])
    file_handler.add_info(info, password)
    new_pass_window.withdraw()
    canvas.delete("all")
    showData()

#Removes password info and reopens login page
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
    root.configure(bg='#ffffff')

    #add title label
    label = tk.Label(root, text="Secure Password Manager", bg='#ffffff') #181818 color
    label.pack(pady=10)

    #Password manager login
    userEntry = tk.Entry(root, width=50)
    passEntry = tk.Entry(root, width=50, show="*")
    submitBtn = tk.Button(root, text="Submit", bg='#ffffff', command=login)
    incorrectLogin = tk.Label(root, text="Incorrect Password or Username", fg="red", bg='#ffffff')
    userEntry.pack(pady=10)
    passEntry.pack(pady=10)
    submitBtn.pack()

    #create canvas
    canvas = tk.Canvas(root, width=600, height=600, bg='#f8f8f8')

    #TODO: create scrollable frame class, remove this from main method.
    #TODO: properly place and center scrollable_frame
    #create scrollable frame
    scrollable_frame = tk.Frame(canvas)

    canvas.create_window((0, 85), window=scrollable_frame, anchor=NW)

    #create scrollbar
    scrollbar = tk.Scrollbar(scrollable_frame, orient=VERTICAL)

    #create inner frame canvas
    info_canvas = tk.Canvas(scrollable_frame, yscrollcommand=scrollbar.set)

    #configure scrollbar to inner canvas
    scrollbar.config(command=info_canvas.yview)

    #create frame in the interior of the inner canvas
    scrollable_frame.interior = interior = tk.Frame(info_canvas)
    interior_id = info_canvas.create_window(0, 0, window=interior, anchor=NW)

    def _configure_interior(event):
        #update scrollbars to match size of inner frame
        size = (interior.winfo_reqwidth(), interior.winfo_regheight())
        info_canvas.config(scrollregion="0 0 %s %s" % size)
        if interior.winfo_reqwidth() != info_canvas.winfo_width():
            #update the canvas's width to fit the inner frame.
            canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

    def _configure_canvas(event):
        if interior.winfo_reqwidth() != info_canvas.winfo_width():
            #update the inner frame's width to fill the canvas
            info_canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


    #add-password and logout buttons
    addBtn = tk.Button(root, text="Add Password", bg='#ffffff', command=addData)
    logoutBtn = tk.Button(root, text="Logout", bg='#ffffff', command=logout)

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
    submitInfoBtn = tk.Button(new_pass_window, text="Submit", bg='#ffffff', command=submitData).pack(pady=10)
    new_pass_window.withdraw()

    #run application
    root.mainloop()