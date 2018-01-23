def CalcCell(f1,f2,h,w,p):
    neibours=[(-1,-1),(1,1),(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,-1)]
    alive, dead = 0,0
    for c in neibours:
        j,i = p[0]+c[0],p[1]+c[1]
        j = j+h if j<0 else j-h if j>=h else j
        i =i+w if i<0 else i-w  if i>=w else i
        alive = alive+1 if f1[j][i]=='X' else alive
        #dead = len(dead+1 if f1[j][i]=='.' else dead
    dead = len(neibours)-alive
    print((p[0],p[1]),':',alive, ' ', dead)
    if f1[p[0]][p[1]]=='.' and alive==3:
        f2[p[0]][p[1]]='X'
    if f1[p[0]][p[1]]=='X' and alive!=3:
        f2[p[0]][p[1]]='.'

h, w = list(map(int,input().split()))
field=[]
nextfield=[]

for j in range(h):
    s=input()[:w]
    field.append(list(s))
    nextfield.append(list(s))

for j in range(h):
    for i in range(w):
        CalcCell(field,nextfield,h,w,(j,i))

for j in range(h):
    print(*nextfield[j],sep='')
