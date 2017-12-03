rows = open('input.txt')

s = 0
for row in rows:
	r = map(int, row.split())
	s += max(r) - min(r)

print('Solution: %d' % (s,))
