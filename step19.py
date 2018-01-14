n,m = map(int,input().split())
bomb,empty='*','.'
f,f1 = [],[]
f.append(empty*(m+2))
for i in range(n):
    f.append(empty+input()[:m]+empty)
    f1.append(['*' for j in range(m)])
f.append(empty*(m+2))

def CalcBombs(f,f1,j,i):
    cells = [f[j][i-1],f[j][i+1],f[j-1][i],f[j+1][i],f[j-1][i-1],f[j+1][i+1],f[j-1][i+1],f[j+1][i-1]]
    f1[j-1][i-1]=cells.count(bomb)

for j in range(1,n+1):
    for i in range(1,m+1):
        if f[j][i]==empty:
            CalcBombs(f,f1,j,i)
        print(f1[j-1][i-1],end='')
    print('',end='\n')
