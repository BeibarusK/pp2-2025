def all_permutations(s):
    if len(s) == 1:
        return [s]
    
    perms = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        
        for p in all_permutations(remaining):
            perms.append(char + p)
    
    return perms
print(all_permutations("abc"))