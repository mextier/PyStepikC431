n = int(input())
print("".join([(str(i)+" ")*i for i in range(1,n+1)])[:n*2].strip())
