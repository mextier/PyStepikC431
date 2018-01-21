#s,ss = input(),input()
s,ss= "abacabadaba","aba"
s1 = list(filter(lambda p:p>=0,sorted(list(set([s.find(ss,i) for i in range(len(s))])))))
print(" ".join([str(i) for i in s1]) if s1 else "-1")
