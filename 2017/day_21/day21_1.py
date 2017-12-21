def rotate_grid(grid):
	g = grid.split('/')
	size = len(g)
	result = ''
	for j in xrange(size):
		result  += ''.join(g[i][size-j-1] for i in xrange(size))
		result += '/'
	return result[:-1]

def flip_grid(grid):
	g = grid.split('/')
	result = ''
	for line in g:
		result += line[::-1]
		result += '/'
	return result[:-1]

def enlarge_2grid(grid):
	global rules
	result = []
	for r in xrange(0, len(grid), 2):
		lines = ['', '', '']
		for c in xrange(0, len(grid), 2):
			g = grid[r][c] + grid[r][c+1] + '/' + grid[r+1][c] + grid[r+1][c+1]
			parts = rules[g].split('/')
			for i,p in enumerate(parts):
				lines[i] += p
		for l in lines:
			result.append(l)
	return result

def enlarge_3grid(grid):
	global rules
	result = []
	for r in xrange(0, len(grid), 3):
		lines = ['', '', '', '']
		for c in xrange(0, len(grid), 3):
			g = grid[r][c:c+3] + '/' + grid[r+1][c:c+3] + '/' + grid[r+2][c:c+3]
			parts = rules[g].split('/')
			for i,p in enumerate(parts):
				lines[i] += p
		for l in lines:
			result.append(l)
	return result

lines = map(lambda x: x.strip(), open('input.txt').readlines())
rules = {}
grid = ['.#.','..#','###']

for line in lines:
	in_grid, out_grid = line.split(' => ')
	rules[in_grid] = out_grid
	for _ in xrange(3):
		in_grid = rotate_grid(in_grid)
		rules[in_grid] = out_grid
	in_grid = flip_grid(in_grid)
	rules[in_grid] = out_grid
	for _ in xrange(3):
		in_grid = rotate_grid(in_grid)
		rules[in_grid] = out_grid

for _ in xrange(5):
	if len(grid) % 2 == 0:
		grid = enlarge_2grid(grid)
	else:
		grid = enlarge_3grid(grid)

print sum(1 for row in grid for c in row if c == '#')