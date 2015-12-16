import re
d={'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}
print [re.findall('(\d+):',l)[0] for l in open('input.txt') if 0==sum([int(x[1])!=d[x[0]] for x in re.findall('(\w+): (\d+)',l)])][0]