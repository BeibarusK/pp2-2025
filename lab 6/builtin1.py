def multiply_all_numbers_in_list(x):
    a=1
    for i in range(len(x)):
        a*=x[i]
    return a

list=[1,2,4,7,8,5,7]
print(multiply_all_numbers_in_list(list))
