p = sorted(map(int, open('input.txt')), reverse=True)
t = sum(p)/4
def distribute(packages, index, target, numDiv):
    global t
    if numDiv == 1:
        return True
    if target == 0:
        return distribute([x for x in packages if not x[1]], 0, t, numDiv-1)
    if target < 0:
        return False
    for i in xrange(index, len(packages)):
        packages[i][1] = True
        result = distribute(packages, i+1, target-packages[i][0], numDiv)
        packages[i][1] = False
        if result:
            return True
    return False

def f(packages, index, target, count, maxCount):
    global t
    if target < 0 or target > 0 and count >= maxCount:
        return (-1,-1)
    if target == 0:
        if distribute([[x[0],False] for x in packages if not x[1]], 0, t, 3):
            quant = reduce(lambda x,y:x*y, [x[0] for x in packages if x[1]], 1)
            return (count, quant)
        else:
            return (-1, -1)
    minQuant = -1
    minCount = -1
    for i in xrange(index, len(packages)):
        packages[i][1] = True
        c,q = f(packages, i+1, target-packages[i][0], count+1, maxCount)
        packages[i][1] = False
        if c >= 0 and (c < minCount or minCount == -1 or c == minCount and q < minQuant):
            minQuant = q
            minCount = c
            maxCount = c
    return (minCount, minQuant)

print f(map(lambda x: [x, False], p), 0, t, 0, len(p))