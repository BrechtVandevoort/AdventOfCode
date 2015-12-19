import re,string
lines = map(lambda x:x.strip(),open('input.txt').readlines())
rul = [re.match('(\w*) => (\w*)',l).groups() for l in lines if '=>' in l]
rules = {r:[x[0] for x in rul if x[1]==r] for r in set([x[1] for x in rul])}
replacements = sorted(rules.keys(),key=len,reverse=True)
mol = lines[-1]
maxLength = max(map(len,replacements))
dyn = [[dict() for x in xrange(len(mol)+1)] for y in xrange(len(mol))]

for length in xrange(1,len(mol)+1):
    print str(length)+'/'+str(len(mol))
    for start in xrange(len(mol)):
        end = start+length
        if end <= len(mol):
            m = mol[start:end]
            if len(m) < maxLength and m[0] not in string.ascii_lowercase:
                dyn[start][end][m] = 0
            if m in rules:
                for r in rules[m]:
                    dyn[start][end][r] = 1
            for k in xrange(start+1,end):
                for left in dyn[start][k]:
                    for right in dyn[k][end]:
                        #print left, right
                        m = left+right
                        if len(m) < maxLength:
                            if not m in dyn[start][end] or dyn[start][k][left]+dyn[k][end][right] < dyn[start][end][m]:
                                dyn[start][end][m] = dyn[start][k][left]+dyn[k][end][right]
                        if m in rules:
                            for r in rules[m]:
                                if not r in dyn[start][end] or dyn[start][k][left]+dyn[k][end][right] < dyn[start][end][r]:
                                    dyn[start][end][r] = dyn[start][k][left]+dyn[k][end][right]+1

print dyn[0][len(mol)]['e']
