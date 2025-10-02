def histogram(x):
    for i in x:
        for z in range(i):
            print('*',end="")
        print()
histogram([4,5,7])