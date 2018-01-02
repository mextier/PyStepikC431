from collections import Counter

marks = input().lower()
l = marks.split(" ")

c = Counter(l)
print("%.2f"%(c["a"]/len(l)))
print("*"*40)
