field = map(lambda x: list(x[:-1]), open('input.txt').readlines())
field_val = lambda c: field[c[0]][c[1]]
apply_direction = lambda c,d: list(x + y for x,y in zip(c, d))
coord = (0,0)
result = ''
direction = (1,0)
possible_directions = {
	(1,0): [(1,0), (0,1), (0,-1)],
	(-1,0): [(-1,0), (0,1), (0,-1)],
	(0,1): [(0,1), (1,0), (-1,0)],
	(0,-1): [(0,-1), (1,0), (-1,0)]
}

while field_val(coord) != '|':
	coord = apply_direction(coord, (0,1))

while field_val(coord) != ' ':
	val = field_val(coord)
	if val not in ' -|+':
		result += val
	elif val == '+':
		for d in possible_directions[direction]:
			if field_val(apply_direction(coord, d)) != ' ':
				direction = d
	coord = apply_direction(coord, direction)

print result