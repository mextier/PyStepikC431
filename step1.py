s=input()
data=[]
while len(s):
    if len(s)==1 and not s[0].isdigit():
        data.append((0,s[0]))
        break
    else:
        data.append((s[0],s[1]))
        s=s[2:]
print(data)
print("*"*40)
