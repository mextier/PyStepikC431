from collections import defaultdict

l = input().lower().split(" ")
dct = defaultdict(int)
for d in sorted(l):
    dct[d] += 1
for k,v in dct.items():
    if v > 1:
        print(str(k))

#lst = input().split()
#print(*[e for e in set(lst) if lst.count(e) > 1])
