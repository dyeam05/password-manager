import os
import csv
import crypto

login_path = "../appdata/login.txt"
data_path = "../appdata/data.enc"

def verify_info(user, password):
    if os.path.isfile(login_path) and os.path.isfile(data_path):
        with open(login_path, 'r') as f:
            line = f.readline()
            savedUser = line.strip()
            line = f.readline()
            savedPass = line.strip()
        if user == savedUser and password == savedPass:
            return True

    else:
        with open(login_path, "x") as f:
            f.write(f"{user}\n")
            f.write(f"{password}\n")
        with open(data_path, "x") as f:
            f.write("")
        return True

def get_info(password):
    empty_info = []
    with open(data_path, 'rb') as f:
        enc_info = f.read()
    
    if os.path.exists(data_path) and os.path.getsize(data_path) == 0:
        dec_info = empty_info
    else:
        dec_info = crypto.decrypt_to_list_of_lists(enc_info, password)
    return dec_info


def add_info(info, password):
    enc_info = crypto.encrypt_list_of_lists(info, password)
    with open(data_path, 'wb') as f:
        f.write(enc_info)
       
