s = map(ord, list('hepxxyzz'))
def i(p):
    global s
    s[p] += 1 if s[p] < 122 else -25
    if s[p] == 97:
        i(p-1)
l = []
while 105 in s or 108 in s or 111 in s or len([1 for x in xrange(6) if s[x] == s[x+1]-1 and s[x] == s[x+2]-2]) == 0 or len(l)<3 and (len(l)<2 or l[0] == l[1]-1):
    i(7)
    l = [x for x in xrange(7) if s[x] == s[x+1]]
print ''.join(map(chr,s))
