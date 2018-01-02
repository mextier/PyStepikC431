s = [" "]+[chr(c) for c in range(ord('a'),ord('z')+1)]
code=int(input().strip())
inputstr = input().strip()
if code>len(s) or code<-len(s):
    code = int(code%len(s))
sd = s[code:] + s[:code]
result = 'Result: "' + ''.join([sd[s.index(c)] for c in inputstr]) + '"'
print(result)
