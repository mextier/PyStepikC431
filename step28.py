

f=[0]
for n in range(int(input())):
    f1=[]
    seq=[]
    for i,d in enumerate(f):
        if d==0:
            f1.append(0)
            f1.append(60)
            f1.append(-120)
            f1.append(60)
            f1.append(0)
        else:
            seq.append(d)
        if seq[::]==[60,-120,60][::]:
            print("replace seq")
            f1.append(60)
            f1.append(60)
            f1.append(-120)
            f1.append(60)
            f1.append(-120)
            f1.append(60)
            f1.append(-120)
            f1.append(60)
            f1.append(60)
            seq.clear()
    f1.extend(seq)
    f[:]=f1[:]
    print(f)


import turtle


turtle.reset()
turtleStep = int(500/len(f))

for d in f:
    turtle.left(int(d))
    turtle.forward(turtleStep)

#f=list(filter(lambda x:x!=0,f))
#print(f)
#print("\n".join(["turn "+str(d) for d in f]))


turtle.exitonclick()
turtle.mainloop()
