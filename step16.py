def genseq(data):
    if not len(data):
        return
    n, c = 0 , data[0]
    for l, i in enumerate(data,1):
        if i!=c:
            yield c if n==1 else str(n)+c
            n,c = 1,i
        else:
            n+=1
        if l==len(data):
            yield c if n==1 else str(n)+c

for d in genseq(input()):
    print(d,end='')
