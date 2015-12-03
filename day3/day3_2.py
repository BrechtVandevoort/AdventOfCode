p = [(0,0),(0,0)]
for x in [(-1,0) if x == '<' else (1,0) if x == '>' else (0,-1) if x == 'v' else (0,1) for x in open('input.txt').readline()]:
    p.append(tuple(a+b for a,b in zip(x,p[-2])))
print len(set(p))
