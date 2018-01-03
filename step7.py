letters = [chr(c) for c in range(ord('A'),ord('Z')+1)]+[chr(c) for c in range(ord('a'),ord('z')+1)]

#instr="3ab4c2CaB"
instr=input()
lp = [(pos, l) for pos, l in enumerate(instr) if l in letters]
lastpos=0
resstr=""
for pos,(N,l) in enumerate(lp,1):
    if lastpos==N:
        num=1
    else:
        num=int(instr[lastpos:N])
    print(str(l)*num,end='')
    lastpos=N+1
