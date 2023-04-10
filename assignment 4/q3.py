def permute(s, l, r, permlist):
    if l == r:
        if s not in permlist:
            permlist.append(s)
    else:
        for i in range(l, r + 1):
            lst = list(s)
            lst[l], lst[i] = lst[i], lst[l]
            s = "".join(lst)
            permute(s, l + 1, r, permlist)
            lst = list(s)
            lst[l], lst[i] = lst[i], lst[l]
            s = "".join(lst)

def PermFinder(s):
    permlist = []
    permute(s, 0, len(s) - 1, permlist)
    return sorted(permlist)

string = input()
permutations = PermFinder(string)
print(permutations)
