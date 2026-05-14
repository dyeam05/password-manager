import os
import crypto


path = "../appdata/test-info.txt"


if os.path.isfile(path):
    print("The file exists!")
else:
    with open(path, "x") as f:
        f.write("This only works if the file is new.")