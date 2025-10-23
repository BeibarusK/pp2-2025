import os

path=input()

if os.path.exists(path):

    if os.access(path, os.R_OK):
        print("Access to reading allowed")
    else:
        print("Access to reading denied")

    if os.access(path, os.W_OK):
        print("Access to writing allowed")
    else:
        print("Access to writing denied")

    if os.access(path, os.X_OK):
        print("Access to execute allowed")
    else:
        print("Access to execute denied")
else:
    print("This path doesn't exist.")