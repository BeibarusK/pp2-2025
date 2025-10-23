import os

path = input()

with open(path, 'r') as file:
    cnt = 0
    for line in file:
        cnt+=1
    print(cnt)