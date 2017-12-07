import re
from collections import defaultdict

def check_balanced(program, programs):
	supporting = programs[program][1]
	weights = [(calc_weight(s, programs), s) for s in supporting]
	
	# If incorrect weight: weight should be different from following 2 weights
	for i, weight in enumerate(weights):
		first_weight = weights[(i+1)%len(weights)]
		second_weight = weights[(i+2)%len(weights)]
		if weight[0] != first_weight[0] and weight[0] != second_weight[0]:
			w = programs[weight[1]][0]
			w += first_weight[0] - weight[0]
			return w
	
	return None

def calc_weight(program, programs):
	weight, supporting = programs[program]
	return weight + sum(calc_weight(s, programs) for s in supporting)

lines = map(lambda x: x.strip(), open('input.txt').readlines())
programs = {}

for line in lines:
	parts = line.split(' -> ')
	program, weight = re.match('(\w+) \((\d+)\)', parts[0]).groups()
	programs[program] = [int(weight), []]
	if len(parts) == 2:
		programs[program][1] = re.findall('\w+', parts[1])

for program in programs:
	result = check_balanced(program, programs)
	if result:
		print result