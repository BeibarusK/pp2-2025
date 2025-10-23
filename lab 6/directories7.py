a_file = input()
b_file = input()


with open(a_file, "r") as a, open(b_file, "w") as b:
        b.write(a.read())