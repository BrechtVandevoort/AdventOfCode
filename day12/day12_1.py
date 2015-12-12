import re
print sum([sum(map(int,re.findall('-?\d+',y))) for y in open('input.txt')])
