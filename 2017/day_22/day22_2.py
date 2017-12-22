from collections import defaultdict

lines = map(lambda x: x.strip(), open('input.txt').readlines())
height = len(lines)
width = len(lines[0])
grid = defaultdict(int) #0: clean, 1: weakened, 2: infected, 3: flagged
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
		grid[(r,c)] = 2 if lines[row][col] == '#' else 0

for _ in xrange(10000000):
	state = grid[pos]
	if state == 0:
		direction = left_turn[direction]
	elif state == 1:
		num_infected += 1
	elif state == 2:
		direction = right_turn[direction]
	elif state == 3:
		direction = right_turn[right_turn[direction]]
	grid[pos] = (grid[pos] + 1) % 4
	pos = tuple(a + b for a, b in zip(pos, direction))

print num_infected