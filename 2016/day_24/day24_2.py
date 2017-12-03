grid = map(lambda x: x.strip(), open('input.txt').readlines())
targets = {value: (r,c) for r, row in enumerate(grid) for c, value in enumerate(row) if value not in '.#'}
directions = [(1,0), (-1,0), (0,1), (0,-1)]
start_pos = targets['0']
queue = [(start_pos, 0, frozenset())]
visited_states = {(start_pos, frozenset())}

while queue:
	old_pos, old_steps, old_visited = queue.pop(0)
	new_steps = old_steps + 1
	for direction in directions:
		new_pos = nr, nc = old_pos[0] + direction[0], old_pos[1] + direction[1]
		if grid[nr][nc] != '#':
			new_visited = set(old_visited)
			if grid[nr][nc] in targets and (grid[nr][nc] != '0' or len(new_visited)+1 == len(targets)):
				new_visited.add(grid[nr][nc])
				if len(new_visited) == len(targets):
					print new_steps
					exit()
			new_visited = frozenset(new_visited)
			if (new_pos, new_visited) not in visited_states:
				visited_states.add((new_pos, new_visited))
				queue.append((new_pos, new_steps, new_visited))
