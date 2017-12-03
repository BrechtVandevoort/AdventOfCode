position = (1,1)
puzzle_input = 1350
target = (31, 39)
directions = [(-1,0), (0,-1), (1,0), (0,1)]
visited = {position}
queue = [(position, 0)]

def is_space(position):
	x, y = position
	s = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
	c = 0
	while s > 0:
		c += s % 2
		s /= 2
	return c % 2 == 0

while True:
	old_pos, old_steps = queue.pop(0)
	steps = old_steps + 1

	for direction in directions:
		pos = tuple(i + j for i,j in zip(old_pos, direction))
		if pos[0] >= 0 and pos[1] >= 0 and pos not in visited and is_space(pos):
			if pos == target:
				print steps
				exit()
			queue.append((pos, steps))
			visited.add(pos)
