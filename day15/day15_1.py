import re,itertools
r = [map(int,re.match('.* (-?\d+).* (-?\d+).* (-?\d+).* (-?\d+).* -?\d+',x).groups()) for x in open('input.txt')]
print max([reduce(lambda y,z:y*z,[max(0,sum(b)) for b in zip(*[[a*x for a in s] for s,x in zip(r,q)])],1) for q in [x+(100-sum(x),) for x in itertools.product(xrange(101),repeat=len(r)-1) if sum(x)<=100]])
