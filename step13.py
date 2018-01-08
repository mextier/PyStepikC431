l=[int(c) for c in input().split()]
n = int(input())
if n in l:
    for pos in [pos for pos,c in enumerate(l,1) if c==n]:
        print(pos-1,sep='',end=' ')
else:
    print("None")
