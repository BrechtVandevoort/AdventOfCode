import re
print max([(2503/(y[1]+y[2])*y[1]+min(y[1],2503%(y[1]+y[2])))*y[0] for y in [map(int, re.match('.* (\d+).* (\d+).* (\d+)',x).groups()) for x in open('input.txt')]])
