from collections import Counter,OrderedDict
s = input()#"Beautiful is better than ugly. Explicit is better than implicit."
l =[len(w) for w in s.split()]
c = Counter(l)
for key in sorted(od.keys()):
    print(str(key) + ": " + str(c[key]))

#od = OrderedDict(sorted(c.items(),key=lambda x:x[0]))
#for k,v in od.items():
    #print(str(k) + ": " + str(v))
