from hashlib import md5

puzzle_input = 'pgflpeqp'
directions = {0: ('U', (-1,0)), 1: ('D', (1,0)), 2: ('L', (0,-1)), 3: ('R', (0,1))}

def get_open_doors(path):
	h = md5(puzzle_input + path).hexdigest()[:4]
	open_doors = []
	for i,v in enumerate(h):
		if v in 'bcdef':
			open_doors.append(directions[i])
	return open_doors

queue = [('', (0,0), 0)]
found = False

while not found:
	path, pos, steps = queue.pop(0)
	open_doors = get_open_doors(path)
	for door in open_doors:
		new_path = path + door[0]
		direction = door[1]
		new_pos = (pos[0] + direction[0], pos[1] + direction[1])
		new_steps = steps + 1
		if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
			if new_pos[0] == new_pos[1] == 3:
				print new_path
				found = True
			else:
				queue.append((new_path, new_pos, new_steps))
