import re
d = [[(t/(y[1]+y[2])*y[1]+min(y[1],t%(y[1]+y[2])))*y[0] for t in xrange(1,2504)] for y in [map(int, re.match('.* (\d+).* (\d+).* (\d+)',x).groups()) for x in open('input.txt')]]
print max([sum([1 if x[i]==max([y[i] for y in d]) else 0 for i in xrange(len(x))]) for x in d])
