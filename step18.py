n1,op,n2 =input().upper().split()
ops = {"PLUS":lambda x,y:int(x+y), "MINUS":lambda x,y:int(x-y),"MULTIPLY":lambda x,y:int(x*y),"DIVIDE":lambda x,y:None if y==0 else int(x/y)}
#import operator
#ops = {"PLUS":lambda x,y:operator.add, "MINUS":operator.sub,"MULTIPLY":operator.mul,"DIVIDE":lambda x,y:operator.floordiv}
print(ops[op](int(n1),int(n2)))
