import os
import csv
import crypto

path = "../appdata/test-info.csv"

def verify_info(user, password):
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

def get_info():
    info = []
    with open(path, 'r') as f:
        f.readline()
        f.readline()
        csvFile = csv.reader(f)
        for line in csvFile:
            print(line)
            info.append(line)
    return info

def add_info(service, user, password):
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([service, user, password])
