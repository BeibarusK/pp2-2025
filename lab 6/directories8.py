import os
path = input()

if os.path.exists(path):
    os.remove(path)
    print("File deleted!")
else:
    print("File not found")