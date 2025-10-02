def palindrome(x):
    y=str(x)
    i=str(x)
    rev=y[::-1]
    if rev==i:
        return True
    else:
        return False
print(palindrome("aziza"))
print(palindrome("455"))