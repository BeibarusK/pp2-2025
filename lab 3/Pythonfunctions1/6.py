def reverse_string(s):
    x=s.split(" ")
    x.sort(reverse=True)
    return x
print(reverse_string("We are ready"))