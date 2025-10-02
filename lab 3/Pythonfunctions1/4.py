def prime_filter(x):
    a=[]
    for i in x:
        if i==1 or i==0:
            pass
        elif i==2 or i==3 or i==5 or i==7:
            a.append(i)
        elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
            pass
        else:
            a.append(i)
    for u in a:
        print(u)
prime_filter([1,3,2,7,11,45,78,37])
