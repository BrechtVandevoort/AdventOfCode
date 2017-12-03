def a(x,v):
    if v>=150 or len(x)==0:
        return v==150
    return a(x[1:],v)+a(x[1:],v+x[0])
print a(map(int,open('input.txt')),0)
