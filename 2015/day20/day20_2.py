v = 33100000/11
sieve = [0 for x in xrange(v)]
found = False
for i in xrange(1,v):
    x = i
    for c in xrange(50):
        if x < v:
            sieve[x] += i
        x += i
print min([i for i in xrange(v) if sieve[i] >= v])
