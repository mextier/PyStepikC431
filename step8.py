n=int(input())
m=int(input())
k=int(input())
if k<=(n-1)*m or k<=(m-1)*n:
    print("YES")
else:
    print("NO")
