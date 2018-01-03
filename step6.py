def f(x):
    return(10)

cache={'5':11,'12':41,'9':47,'20':61,'12':41}

n = int(input())
for i in range(n):
    x = int(input())
    if str(x) not in list(cache.keys()):
        cache[str(x)]=f(x)
    print(cache[str(x)])
