import os

path = input()

directories=[]
files = []
everything = os.listdir(path)

if os.path.exists(path):
    for item in everything:
        full_path = os.path.join(path, item)
        if os.path.isdir(path):
            directories.append(item)
    
        elif os.path.isfile(path):
            files.append(item)
else:
    print("this path doesnt exist")

print("Directories")
for d in directories:
    print(d)

print("Files")
for f in files:
    print(f)

print("All Directories and Files")
for item in everything:
    print(item)
