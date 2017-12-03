from itertools import permutations

def solve_row(row):
	for x,y in permutations(row, 2):
		if x % y == 0:
			return x / y


rows = open('input.txt')

s = 0
for row in rows:
	r = map(int, row.split())
	s += solve_row(r)

print('Solution: %d' % (s,))
