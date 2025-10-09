n=int(input())

def is_even_nums(x):
    cnt = 1
    while cnt <= x:
        if cnt%2==0:
            yield cnt
        cnt += 1
a=is_even_nums(n)

print(",".join(str(i) for i in a))