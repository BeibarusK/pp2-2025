def is_palindrome(x):
    a=x[::-1]
    if len(x)==1:
        print("YES")
    elif x==a:
        print("YES")
    else:
        print("NO")

x="Dostoevsky"
y="aba"

is_palindrome(x)
is_palindrome(y)