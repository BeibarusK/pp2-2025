n=int(input())
def divisions_by_3_and_4(x):
    cnt=0
    while cnt <= x:
        if cnt%3==0 and cnt%4==0:
            yield cnt
        cnt+=1
a=divisions_by_3_and_4(n)
for i in a:
    print(i)