print(''.join([w if w[0].upper()==w[0] else w[0].upper()+w[1:] for w in input().split("_")]))
