import re,itertools
l = [re.match('(\w*) to (\w*) = ([0-9]*)', x).groups() for x in open('input.txt')]
c = list(set([x[0] for x in l]+[x[1] for x in l]))
d = {tuple(sorted((x,y))):int(z) for x,y,z in l}
print min([sum([d[tuple(sorted((p[i],p[i+1])))] for i in xrange(len(p)-1)]) for p in itertools.permutations(c)])
