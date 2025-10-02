def unique_elements(x):
    u=[]
    x.sort()
    for i in range(len(x)):
        if i==len(x)-1:
            u.append(x[i])
        else:
            if x[i]==x[i+1]:
                pass
            else:
                u.append(x[i])
    return u
print(unique_elements([1,1,4,5,7,7,8,8,8,8,9]))