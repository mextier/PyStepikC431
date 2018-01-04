instr="3ab4c2CaB"

def decodeseq(seq):
    return(str(seq[1])*int(seq[0]))

def genseq(data):
    n = ""
    for i in data:
        if i.isdigit():
            n = n + str(i)
        else:
            if not len(n):
                n="1"
            yield (int(n),i)
            n=""


for seq in genseq(instr):
    print(decodeseq(seq),end='')
