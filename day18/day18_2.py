l = [[0 for x in xrange(102)]]
l+= [[0]+[int(x=='#') for x in i.strip('\n')]+[0] for i in open('input.txt')]+l
l[1][1] = l[1][100] = l[100][1] = l[100][100] = 1
def c(l):
    r = [[0 for y in x] for x in l]
    for i in xrange(1,101):
        for j in xrange(1,101):
            n = sum([l[x][y] for x in [i-1,i,i+1] for y in [j-1,j,j+1]])-l[i][j]
            r[i][j] = int(l[i][j] and n==2 or n==3)
    r[1][1] = r[1][100] = r[100][1] = r[100][100] = 1
    return r
for x in xrange(100):
    l = c(l)
print sum(map(sum,l))
