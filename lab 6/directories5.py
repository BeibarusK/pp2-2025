path = input()

with open(path, 'a') as file:
    list=[1,2,3,7,8,9,4,50,"Dostoevsky"]
    file.write(list)

with open(path, 'r') as file:
    file.read()