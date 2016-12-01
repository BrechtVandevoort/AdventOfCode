instructions = open('input.txt').read().strip().split(', ')
position = [0,0]
direction = 0
for i in instructions:
	rotation = -1 if i[0] == 'L' else 1
	direction = (direction + rotation) % 4
	distance = int(i[1:])
	if direction > 1:
		distance *= -1
	position[direction % 2] += distance
print sum(map(abs, position))
