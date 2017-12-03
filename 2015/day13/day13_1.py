import re,itertools
m = [re.match('(\w+).* (l|g).* (\d+).* (\w+)',x).groups() for x in open('input.txt')]
d = {(r[0],r[3]):int(r[2]) if r[1]=='g' else -int(r[2]) for r in m}
n = set([r[0] for r in m])
print max([sum([d[(p[i],p[(i+1)%len(p)])]+d[(p[(i+1)%len(p)],p[i])] for i in xrange(len(p))]) for p in itertools.permutations(n)])
