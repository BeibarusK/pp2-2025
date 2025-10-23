import os

path = input()

if os.path.exists(path):
    print("Path exists yo")
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    print(directory, filename)
else:
    print("Path doesnt exist")