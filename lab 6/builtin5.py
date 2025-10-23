def are_tuple_elements_true(x):
    a=list(x)
    y=0
    while y < len(a):
        z=bool(a[y])
        print(z)
        if z:
            y+=1
            pass
        else:
            break
    if y==len(a):
        return True
    else:
        return False
x=(1,4,5,-1,7,8,False)
print(are_tuple_elements_true(x))
    
    