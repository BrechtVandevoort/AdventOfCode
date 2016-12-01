instructions = open('input.txt').read().strip().split(', ')
position = [0,0]
visited = [[0,0]]
direction = 0
for i in instructions:
	rotation = -1 if i[0] == 'L' else 1
	direction = (direction + rotation) % 4
	distance = int(i[1:])
	step = -1 if direction > 1 else 1
	for j in range(distance):
		position[direction % 2] += step
		if position in visited:
			print sum(map(abs, position))
		else:
			visited.append(position[:])
