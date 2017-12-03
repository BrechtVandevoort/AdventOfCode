v = 3310000
sieve = [0 for x in xrange(v)]
found = False
for i in xrange(1,v):
    x = i
    while x < v:
        sieve[x] += i
        x += i
print min([i for i in xrange(v) if sieve[i] >= v])
