import re
lines = map(lambda x:x.strip(),open('input.txt').readlines())
rul = [re.match('(\w*) => (\w*)',l).groups() for l in lines if '=>' in l]
rules = {r:[x[1] for x in rul if x[0]==r] for r in set([x[0] for x in rul])}
mol = lines[-1]
s = set()
for i in xrange(len(mol)):
    for j in xrange(i+1,i+1+max(map(len,rules))):
        if j <= len(mol) and mol[i:j] in rules:
            for r in rules[mol[i:j]]:
                s.add(mol[:i] + r + mol[j:])
print len(s)
