path = open('input.txt').read().strip().split(',')
target = [0,0]
pos = [0,0]
steps = 0
directions = {
	'n': lambda x: [x[0]+1, x[1]],
	'nw': lambda x: [x[0]+0.5, x[1]-0.5],
	'ne': lambda x: [x[0]+0.5, x[1]+0.5],
	's': lambda x: [x[0]-1, x[1]],
	'sw': lambda x: [x[0]-0.5, x[1]-0.5],
	'se': lambda x: [x[0]-0.5, x[1]+0.5]
}

for p in path:
	target = directions[p](target)

while pos != target:
	if pos[1] == target[1]:
		pos[0] += 1 if target[0] > pos[0] else -1
	else:
		pos[0] += 0.5 if target[0] > pos[0] else -0.5
		pos[1] += 0.5 if target[1] > pos[1] else -0.5
	steps += 1

print steps