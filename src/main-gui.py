import tkinter as tk
import hashlib
import file_check

logged_in = False

def login():
    user_input = userEntry.get()
    pass_input = passEntry.get()
    hashed_pass = hashlib.sha256(pass_input.encode())
    hex_pass = hashed_pass.hexdigest()
    print(f"user name: {user_input}")
    print(f"pass input: {pass_input}")
    print(f"hashed pass: {hex_pass}")
    validLogin = file_check.verify_info(user_input, hex_pass)
    if validLogin:
        print("successful login")
        
    else:
        incorrectLogin.pack()


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

root.mainloop()