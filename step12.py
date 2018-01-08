n = int(input())
while n!=1:
    print(str(n),'',end='')
    n = n//2 if n%2==0 else 1+3*n
print(n)

l = [int(input())]
while l[-1:][0]!=1:
    l.append(l[-1]//2 if l[-1]%2==0 else 1+3*l[-1])
print(" ".join(str(c) for c in l))
