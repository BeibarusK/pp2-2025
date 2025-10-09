n=int(input())

def to_zero(x):
    while x>=0:
        yield x
        x-=1

a=to_zero(n)
for i in a:
    print(i)