eta, inp = dict( m=1.00, mile = 1609, yard = 0.9144, foot = 0.3048, inch = 0.0254, km = 1000, cm = 0.01, mm = 0.001 ), input().split()
x = float(inp[0]) * eta[inp[1]] / eta[inp[3]]
print('{:.2e}'.format(x))
