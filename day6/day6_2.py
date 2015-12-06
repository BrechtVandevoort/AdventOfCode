import re
g = [[0 for x in range(1000)] for y in range(1000)]
for x in open('input.txt'):
    r = re.match('(?:turn )*(\w*) (\d*),(\d*) \w* (\d*),(\d*)',x).groups()
    for i,j in [(i,j) for i in xrange(int(r[1]),int(r[3])+1) for j in xrange(int(r[2]),int(r[4])+1)]:
        g[i][j] = max(0, g[i][j]+(2 if r[0][0]=='t' else 1 if r[0]=='on' else -1))
print sum([sum(i) for i in g])
