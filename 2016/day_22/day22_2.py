import re

directions = [(0,1), (0,-1), (1,0), (-1,0)]
width, height = 33, 30
puzzle_input = open('input.txt').readlines()[2:]
nodes = map(lambda x: map(int, re.match('\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)', x).groups()), puzzle_input)

grid = [[False for _ in range(width)] for _ in range(height)]
start_pos = (0,0)
for node in nodes:
	grid[node[1]][node[0]] = node[3] < 100
	if node[3] == 0:
		start_pos = (node[1], node[0])

data_pos = (0, width-1)
queue = [(start_pos, data_pos, 0)]
visited = {(start_pos, data_pos)}

while queue:
	old_pos, old_data_pos, old_steps = queue.pop(0)
	new_steps = old_steps+1
	for d in directions:
		nr, nc = new_pos = (old_pos[0] + d[0], old_pos[1] + d[1])
		if 0 <= nr < height and 0 <= nc < width and grid[nr][nc]:
			new_data_pos = old_pos if new_pos == old_data_pos else old_data_pos
			if (new_pos, new_data_pos) not in visited:
				queue.append((new_pos, new_data_pos, new_steps))
				visited.add((new_pos, new_data_pos))
			if new_data_pos == (0,0):
				print new_steps
				queue = []
