def knot_hash(s):
	index = lambda x: x % 256
	lengths = map(ord, s) + [17, 31, 73, 47, 23]
	skip = 0
	pos = 0
	lst = list(xrange(256))
	hashed = ''

	for _ in xrange(64):
		for length in lengths:
			stack = [lst[index(pos + x)] for x in xrange(length)]
			for x in xrange(length):
				lst[index(pos + x)] = stack.pop()
			pos += length + skip
			skip += 1

	for i in xrange(16):
		block = lst[16*i : 16*(i+1)]
		xor = reduce(lambda x,y: x^y, block)
		hashed += format(xor, '08b')

	return hashed

def is_valid(coord):
	return 0 <= coord[0] < 128 and 0 <= coord[1] < 128

def clear_region(field, coord):
	directions = [(-1,0), (1,0), (0,-1), (0,1)]
	
	if is_valid(coord) and field[coord[0]][coord[1]] == 1:
		field[coord[0]][coord[1]] = 0
		for direction in directions:
			new_coord = tuple(c + d for c,d in zip(coord, direction))
			clear_region(field, new_coord)


puzzle_input = 'xlqgujun'
field = []
regions = 0

for x in xrange(128):
	h = knot_hash(puzzle_input + '-' + str(x))
	field.append(map(int, h))

for x in xrange(128):
	for y in xrange(128):
		if field[x][y]:
			regions += 1
			clear_region(field, (x,y))

print regions