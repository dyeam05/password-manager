import tkinter as tk

def show_text():
    user_input = userEntry.get()
    pass_input = passEntry.get()
    print(f"user name: {user_input}")
    print(f"pass input: {pass_input}")


root = tk.Tk()
root.title("Password Manager")
root.geometry("750x750")

label = tk.Label(root, text="Secure Password Manager")
label.pack(pady=10)

userEntry = tk.Entry(root, width=50)
passEntry = tk.Entry(root, width=50, show="*")
submitBtn = tk.Button(root, text="Submit", command=show_text)

userEntry.pack(pady=10)
passEntry.pack(pady=10)
submitBtn.pack()

root.mainloop()