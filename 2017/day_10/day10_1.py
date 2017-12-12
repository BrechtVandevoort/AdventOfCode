def index(x):
	return x % 256

lengths = map(int, open('input.txt').read().strip().split(','))
skip = 0
pos = 0
lst = list(xrange(256))

for length in lengths:
	stack = [lst[index(pos + x)] for x in xrange(length)]
	for x in xrange(length):
		lst[index(pos + x)] = stack.pop()
	pos += length + skip
	skip += 1
	
print lst[0] * lst[1]