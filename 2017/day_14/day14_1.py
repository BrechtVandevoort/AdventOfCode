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


puzzle_input = 'xlqgujun'
used = 0

for x in xrange(128):
	h = knot_hash(puzzle_input + '-' + str(x))
	used += sum(map(int, h))

print used