import re
def s(x):
    global m,c,d
    if re.match('[0-9]+',x):
        return int(x)
    if not x in m:
        m[x] = d[c[x][1]](c[x][0], c[x][2])
    return m[x]
d = {'': lambda x,y: s(x), 'AND': lambda x,y: s(x) & s(y), 'OR': lambda x,y: s(x) | s(y), 'NOT': lambda x,y: 65535 & ~s(y), 'LSHIFT': lambda x,y: 65535 & (s(x) << int(y)), 'RSHIFT': lambda x,y: s(x) >> int(y)}
c = {}
m = {}
for r in open('input.txt'):
    g = re.match('([a-z0-9]*) ?([A-Z]*) ?([a-z0-9]*) -> ([a-z]*)', r).groups()
    c[g[3]] = g
print s('a')
