n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
for j in range(m):
    print(" ".join(str(mat[i][j]) for i in range(n)),end='\n')


#print(*mat)
#print(zip(*mat))
