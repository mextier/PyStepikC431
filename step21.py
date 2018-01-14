a,b = map(int,input().split('/'))
while b:
    print(int(a/b),end=' ')
    a,b = b,a%b
