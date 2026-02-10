from itertools import permutations

s = "ABC"

perms = permutations(s)

for p in perms:
    print("".join(p))
