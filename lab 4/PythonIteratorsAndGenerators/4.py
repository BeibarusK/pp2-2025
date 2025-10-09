a=int(input())
b=int(input())

def squares(x, y):
    while x<=y:
        yield x**2
        x+=1

f=squares(a, b)
for i in f:
    print(i)