def modify_list(l):
    #l[:]=filter(lambda x: x % 2==0,l)
    #l[:]=map(lambda x:int(x/2),l)
    l[:] = [i//2 for i in l if i%2 == 0]


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
