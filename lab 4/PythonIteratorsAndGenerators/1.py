N=int(input())
def fun(x):
    cnt = 1
    while cnt <= x:
        yield cnt**2
        cnt += 1
ctr = fun(N)
for n in ctr:
    print(n)