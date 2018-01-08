l=input().upper().split()
m = input().upper()
#l="7C 10H".split()
#m = "S"

digits="6 7 8 9 10 J Q K A".split()

k1 = (l[0][0:len(l[0])-1],l[0][-1:])
k2 = (l[1][0:len(l[1])-1],l[1][-1:])

print("Error" if m not in [k1[1],k2[1]] and k1[1]!=k2[1] else "First" if k1[1]==m and k2[1]!=m else "Second" if k2[1]==m and k1[1]!=m else "Error" if digits.index(k1[0])==digits.index(k2[0]) else "First"
 if digits.index(k1[0])>digits.index(k2[0]) else "Second")
