import os
import crypto

def verify_info(user, password):
    path = "../appdata/test-info.txt"


    if os.path.isfile(path):
        print("The file exists!")
        with open(path, 'r') as f:
            line = f.readline()
            savedUser = line.strip()
            line = f.readline()
            savedPass = line.strip()
        if user == savedUser and password == savedPass:
            return True

    else:
        with open(path, "x") as f:
            f.write(f"{user}\n")
            f.write(f"{password}\n")
        return True