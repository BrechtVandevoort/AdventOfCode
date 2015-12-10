import itertools
s = '1321131112'
for i in xrange(50):
    s = ''.join([str(len(list(v)))+str(k) for k,v in itertools.groupby(s)])
print len(s)
