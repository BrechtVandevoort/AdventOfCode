import re

lines = map(lambda x: x.strip(), open('input.txt').readlines())
programs = {}

for line in lines:
	parts = line.split(' -> ')
	program, weight = re.match('(\w+) \((\d+)\)', parts[0]).groups()
	programs[program] = [weight, []]
	if len(parts) == 2:
		programs[program][1] = re.findall('\w+', parts[1])
	
supporting_set = set(programs.keys())
supported_set = set()
for program, info in programs.iteritems():
	supported_set |= set(info[1])

root_set = supporting_set - supported_set
print root_set.pop()