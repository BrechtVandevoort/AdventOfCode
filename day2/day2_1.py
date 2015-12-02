l = [line.rstrip('\n') for line in open('input.txt')]
print sum([2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[0]*x[2] + x[0]*x[1]*x[2]/max(x) for x in [map(int,x) for x in [x.split('x') for x in l]]])
