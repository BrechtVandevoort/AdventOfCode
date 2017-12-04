from collections import defaultdict

def calc_value(coords, values):
	s = 0
	for x in xrange(coords[0]-1, coords[0]+2):
		for y in xrange(coords[1]-1, coords[1]+2):
			s += values[(x,y)]
	return s


puzzle_input = 289326

coords = (0,0)
values = defaultdict(int)
values[tuple(coords)] = 1
direction = (1,0)
size = 1
steps = 0

while values[coords] <= puzzle_input:
	coords = tuple(x+y for x,y in zip(coords, direction))
	steps += 1
	values[coords] = calc_value(coords, values)

	if steps == size:
		steps = 0
		if direction == (1,0):
			direction = (0,-1)
		elif direction == (0,-1):
			direction = (-1,0)
			size += 1
		elif direction == (-1,0):
			direction = (0,1)
		else:
			direction = (1,0)
			size += 1

print values[coords]
