from collections import Counter

words = input().lower().split(" ")
c = Counter(words)
for k,v in c.items():
    print(k + " " + str(v))
