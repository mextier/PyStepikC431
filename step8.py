data=input().upper()
#data = "IX"

rdict1 = {"I":1,"V":5,"X":10,"L":50, "C":100, "D":500,"M":1000}
rdict2 = {'CM':900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
s,i = 0,0
while i<len(data):
    if i==len(data) -1:
        s+=int(rdict1[data[i]])
    else:
        if data[i:i+2] in rdict2.keys():
            s+=int(rdict2[data[i:i+2]])
            i+=1
        else:
            s+=int(rdict1[data[i]])
    i+=1

print(s)
