import re
a=lambda x,y:x!=y
b=lambda x,y:x>=y
c=lambda x,y:x<=y
d={'children':(a,3),'cats':(c,7),'samoyeds':(a,2),'pomeranians':(b,3),'akitas':(a,0),'vizslas':(a,0),'goldfish':(b,5),'trees':(c,3),'cars':(a,2),'perfumes':(a,1)}
print [re.findall('(\d+):',l)[0] for l in open('input.txt') if 0==sum([d[x[0]][0](int(x[1]),d[x[0]][1]) for x in re.findall('(\w+): (\d+)',l)])][0]