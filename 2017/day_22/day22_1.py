from collections import defaultdict

lines = map(lambda x: x.strip(), open('input.txt').readlines())
height = len(lines)
width = len(lines[0])
grid = defaultdict(int)
pos = (0,0)
direction = (-1, 0)
right_turn = {
	(-1,0): (0,1),
	(0,1): (1,0),
	(1,0): (0,-1),
	(0,-1): (-1,0)
}
left_turn = {
	(-1,0): (0,-1),
	(0,1): (-1,0),
	(1,0): (0,1),
	(0,-1): (1,0)
}
num_infected = 0

for row in xrange(height):
	for col in xrange(width):
		r = row - height / 2
		c = col - width / 2
		grid[(r,c)] = 1 if lines[row][col] == '#' else 0

for _ in xrange(10000):
	state = grid[pos]
	if state == 1:
		direction = right_turn[direction]
	else:
		direction = left_turn[direction]
		num_infected += 1
	grid[pos] = 1 - grid[pos]
	pos = tuple(a + b for a, b in zip(pos, direction))

print num_infected