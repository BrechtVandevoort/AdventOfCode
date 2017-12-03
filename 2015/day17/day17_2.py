n = m = 0
def a(x,v,c):
    global m,n
    if v==150:
        if c<n or n==0:
            n = c
            m = 1
        elif c==n:
            m += 1
    elif v<150 and len(x)>0:
        a(x[1:],v,c)
        a(x[1:],v+x[0],c+1)
a(map(int,open('input.txt')),0,0)
print m
