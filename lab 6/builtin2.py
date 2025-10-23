def number_of_upp_and_low_let(x):
    sum=0
    for i in x:
        y=str(i)
        if y.isupper() or y.islower():
            sum+=1
    return sum

print(number_of_upp_and_low_let("Dostoevsky wrote a novel in 29 days!"))
