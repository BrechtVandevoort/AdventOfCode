print len([x for x in open('input.txt') if x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')>2 and x.count('ab')+x.count('cd')+x.count('pq')+x.count('xy')==0 and len([i for i in xrange(len(x)) if i>0 and x[i-1]==x[i]])>0])